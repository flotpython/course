#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import time
import urllib.request, urllib.error, urllib.parse
from operator import itemgetter

logging.basicConfig(
    filename='diagnose.log',
    filemode='w',
    level=logging.ERROR)

# À propos du module de la librairie standard logging.
# J'utilise ici le module logging qui permet de définir différents 
# niveaux de log pour debugger un programme et pour faire des fichiers
# de trace d'exécution. J'ai laissé dans ce fichier tous les logs que 
# j'ai utilisés pour debugger ce programme. Pour voir tous les logs
# il faut mettre ci-dessus le paramètre level a logging.DEBUG (mais
# attention ça va faire beaucoup de donnees).


# helper function
def extract_domains_from_url(url):
    """
    Extrait un domaine d'une URL

    Retourne le tuple T qui contient
    T[0]: domaine avec le bon protocol (http://domain or https://domain)
    T[1]: domaine sans le protocol (sans http:// or https://)
    """
    protocol_http = 'http://' 
    protocol_https = 'https://' 
    protocol = ''
    if url.startswith(protocol_http):
        url = url.replace(protocol_http, '')
        protocol = protocol_http
    elif url.startswith(protocol_https):
        url = url.replace(protocol_https, '')
        protocol = protocol_https
    else:
        logging.debug("Erreur lors de l'extraction du domaine: " + url)
        return ''
    domain = url[:url.find('/')]
    return (protocol + domain, domain)

# helper function
def is_html_page(url):
    """
    simple heuristique pour tester si une page est écrite en
    HTML. Il y a des cas mal identifiés par cette heuristique,
    mais elle est suffisante pour nos besoins. Par exemple:
    http://inria.fr sera identifié comme non html, de même que
    toutes les pages qui utilisent des points dans le nom d'un
    répertoire.
    """
    # if there is no extension, it is a directory, so it
    # defaults to an index.html page
    if url.endswith('/'):
        return True
    else:
        url_tokens = url.split('/')
        # if there is no extension, it is a directory, so it
        # defaults to an index.html page
        if '.' not in url_tokens[-1]:
            return True
        elif ('html' in url_tokens[-1].lower() or   
              'htm' in url_tokens[-1].lower()):
            return True
        else:
            return False

class HTMLPage(object):
    """
    représente une page HTML. 

    L'objet a 4 attributs:
        * url: l'URL qui correspond a la page Web
        * _html_it: un itérateur qui parcourt le code HTML, une ligne 
                   à la fois
        * urls: la liste de toutes les URLs contenues dans la page
        * http_code: le code retourné par le protocol HTTP lors de 
                    l'accès à la page
          * http_code=0 signifie une erreur dans l'URL, 
          * http_code=-1 signifie que le site de répond pas
          * http_code=-2 signifie une exception en accédant à l'URL
    """

    def __init__(self, url):
        """
        Constructeur de la classe. Le constructeur prend comme
        argument une URL et construit un objet HTMLPage en définissant
        les 4 attributs url, _html_it, urls, http_code
        """
        self.http_code = 0
        self.url = url
        self._html_it = self.page_fetcher(self.url)
        self.urls = self.extract_urls_from_page()
        logging.debug('+'*80 + '\npage {}\n'.format(self.url))
        logging.debug('extracted URLs {}\n'.format(self.urls) + '+'*80 + '\n')

    def page_fetcher(self, url):
        """
        accede a l'URL et retourne un objet qui permet de parcourir le
        code HTML (voir la documentation de urllib.request.urlopen) ou une
        liste vide en cas d'erreur.
        """
        
        # surcharge la classe Request pour faire des requetes HEAD qui
        # pemettent de collecter que l'entete de la page. C'est utile
        # lorsque la page ne contient pas de code HTML et donc pas
        # d'URL.  On peut ainsi obtenir un code HTTP sans avoir besoin
        # de telecharger toute la page.
        class HeadRequest(urllib.request.Request):
            def get_method(self):
                return "HEAD"
        
        try:
            if is_html_page(url):
                page = urllib.request.urlopen(url)
            else:
                logging.debug('HEAD request for {}'.format(url))
                page = urllib.request.urlopen(HeadRequest(url))
            self.http_code = page.getcode()
            return page
        except urllib.error.HTTPError as e:
            logging.warning('HTTPError: cannot open {}. Reason {}, code {}'
                            .format(url, e.reason, e.code))
            self.http_code = e.code
            return []

        except urllib.error.URLError as e:
            logging.warning('URLError: cannot open {}. Reason {}'
                            .format(url, e.reason))
            self.http_code = -1
            return []
        except Exception as e:
            logging.error('uncatched error {}\nfor URL {}'.format(e, url))
            self.http_code = -2
            return []

    def extract_urls_from_page(self):
        """
        Construit la liste de toutes les URLs contenues dans le corps de
        la page HTML en parcourant l'itérateur retourné par
        page_fetcher()

        On identifie une URL parce qu'elle est précédée de href= et
        dans le corps (body) de la page. Le parsing que l'on implemente
        est imparfait, mais un vrai parsing intelligent demanderait
        une analyse syntaxique trop complexe pour nos besoins.
        
        Plus en détails, notre parsing consiste à chercher dans le
        corps de la page (body): 

        - les urls contenues dans le champ href (essentiellement on
          cherche le tag 'href=' et on extrait ce qui est entre
          guillemets ou apostrophes)
         
        - on ne garde ensuite que les urls qui commencent par http ou
          https et
             
             * les urls qui commencent par ./ auxquelles on ajoute
               devant (a la place du point) l'Url de la page d'origine
               (self.url) exemple : pour './ma_page.html' et self.url =
               http://mon_site.fr/rep1/ on obtient l'url
               http://mon_site.fr/rep1/ma_page.html
          
            * les urls qui commencent par /ma_page.html auxquelles on
              ajoute devant uniquement le hostname de la page d'origine
              (self.url) exemple : pour '/ma_page.html' et self.url =
              http://mon_site.fr/rep1/ on obtient l'url
              http://mon_site.fr/ma_page.html

        Cette méthode retourne la liste des URLs contenues dans la
        page.

        """

        # parse the page to extract all URLs in href field and in the
        # body of the document
        list_urls = []
        is_body = False
        for byte_line in self._html_it:
            line = str(byte_line)
            # line = line.lower()
            if is_body:
                if "href=" in line.lower():
                    # extract everything between href=" and "> probably
                    # not bullet proof, but should work most of the
                    # time. 
                    url_separator = line[line.lower().find('href=') + 5]
                    line = line[line.lower().find('href=') + 6:]
                    line = line[:line.lower().find(url_separator)]

                    list_urls.append(line)
                elif "http://" in line or "https://" in line:
                    logging.debug('this URL was not extracted: ' + line)
            else:
                # do not end with > in order to deal with arguments
                # without complexe parsing
                if '<body' in line:
                    is_body = True

                    
        logging.debug('in extract_urls_from_page\n' + '-'*80 + '\n')
        logging.debug('All extracted URLs:\n')
        logging.debug('{}\n'.format(list_urls))
        # keep only http and https
        filtered_list_urls = [x for x in list_urls
                              if x.lower().startswith('http')
                              or x.lower().startswith('https')]

        logging.debug('filtered URLs (http, https):\n')
        logging.debug('{}\n'.format(filtered_list_urls))
        # and reconstruct relative links ./
        filtered_list_urls.extend([self.url[:self.url.rfind('/')] + x[1:]
                                   for x in list_urls
                                   if x.startswith('./')])
        logging.debug('filtered URLs (relatives ./):\n')
        logging.debug('{}\n'.format(filtered_list_urls))

        # and reconstruct relative links /
        filtered_list_urls.extend([extract_domains_from_url(self.url)[0] 
                                   + x for x in list_urls
                                   if x.startswith('/')]) 

        logging.debug('filtered URLs (relatives /):\n')
        logging.debug('{}\n'.format(filtered_list_urls))

        # debug
        # print [x for x in list_urls if x.startswith('./')]

        return list(set(filtered_list_urls))


class Crawler(object):
    """
    Cette classe permet de creer l'objet qui va gerer le crawl. Cet
    objet est iterable et l'iterateur va, a chaque tour, retourner un
    nouvel objet HTMLPage.

    L'instance du crawler va avoir comme principaux attributs 
      * l'ensemble des pages a crawler pages_to_be_crawled
      * l'ensemble des pages deja crawles pages_crawled
      * un dictionnaire qui a chaque URL fait correspondre la liste de 
      toutes les pages qui ont reference cette URL lors du crawl 
      pages_to_be_crawled_dict
    """

    def __init__(self, seed_url, max_crawled_pages=10 ** 10,
                 page_filter=None):
        """
        Constructeur du crawler

        Le constructeur prend comme arguments
        -seed_url: l'URL de la page a partir de laquelle on demarre le crawl
        -max_crawled_pages: le nombre maximum de pages que l'on va crawler
        (10**10 par defaut)
        -page_filter: la liste des pages sur lesquels le crawler 
        doit rester (pas de filtre par defaut). Typiquement, une URL 
        passe le filtre si n'importe lequel des elements de page_filter
        est contenu dans l'URL
        """
        if page_filter is None:
            page_filter = []
        self.page_filter = page_filter
        self.seed_url = seed_url
        self.max_crawled_pages = max_crawled_pages

        # Each key is a URL, and the value for the key url is the list
        # of pages that referenced this url. This dict is used to find
        # pages that reference given URLs in order to diagnose
        # buggy Web pages.
        self.pages_to_be_crawled_dict = {}

        # set of the pages still to be crawled
        self.pages_to_be_crawled = set()

        # set of the pages/domains already crawled
        self.pages_crawled = set()
        self.domains_crawled = set()
        
        # duration of the last crawl
        self.last_crawl_duration = 0

    def update_pages_to_be_crawled(self, page):
        """
        Prend un objet HTMLpage comme argument et trouve toutes les
        URLs presente dans la page HTML correspondante. Cette methode
        met a jour le dictionnaire pages_to_be_crawled_dict et
        l'ensemble pages_to_be_crawled. On ne met pas a jour le
        dictionnaire et le set si l'URL correspondant a l'objet
        HTMLpage n'est pas dans la liste de pages acceptees dans
        self.page_filter.
        """
        # check if the page from which we got URLs pass the page_filter
        pass_filter = False
        for p in self.page_filter:
            if p in page.url:
                pass_filter = True

        logging.debug('*'*80 + '\n')
        logging.debug('page crawled providing the URLs : {}\n'.format(page.url))
        logging.debug('pass filter state: {}\n'.format(pass_filter))
        if pass_filter:
            logging.debug('passes the filter \n')
            logging.debug('list of urls to be added: {}'.format(page.urls))
            # update the list of pages to be crawled with the URLs
            for url in page.urls:
                # update the dict even if url already crawled (to get
                # comprehensif information)
                if url in self.pages_to_be_crawled_dict:
                    self.pages_to_be_crawled_dict[url].append(page.url)
                else:
                    self.pages_to_be_crawled_dict[url] = [page.url]

                # update the set if url not already crawled
                if url not in self.pages_crawled:
                    self.pages_to_be_crawled.add(url)


    def __repr__(self):
        """
        permet d'afficher simplement des informations sur l'etat
        courant du crawl.

        retourne une chaine de caracteres donnant:
        -le nombre de pages et domaines deja crawle
        -le nombre de pages encore a crawler
        -la duree du dernier crawl
        """
        output = ('#' * 60 + '\nInitial URL: {}'.format(self.seed_url)
                   + '\nPages/domains already crawled {}/{}'.format(
                 len(self.pages_crawled),
                 len(self.domains_crawled))
                   + '\nPages to be crawled {}'.format(
                 len(self.pages_to_be_crawled))
                   + '\n crawl duration {}'.format(
                 self.last_crawl_duration)
                  )
        return output

    def __iter__(self):
        """
        Cette methode est implementee comme une fonction generatrice. A
        chaque appel de next() sur l'iterateur, on obtient un nouvel
        objet HTMLPage qui correspond a une URL qui etait dans
        l'ensemble des URLs a crawler. 

        On ne donne aucune garantie sur l'ordre de parcours des URLs
        """

        # case of the first page
        start_time = time.time()
        page = HTMLPage(self.seed_url)
        self.last_crawl_duration = time.time() - start_time
        self.pages_crawled.add(seed_url)
        self.domains_crawled.add(extract_domains_from_url(seed_url)[1])
        self.update_pages_to_be_crawled(page)
        yield page 
        
        # all the other pages
        while (self.pages_to_be_crawled and
                       len(self.pages_crawled) < self.max_crawled_pages):
            url = self.pages_to_be_crawled.pop()
            start_time = time.time()
            page = HTMLPage(url)
            self.last_crawl_duration = time.time() - start_time
            self.pages_crawled.add(url)
            self.domains_crawled.add(extract_domains_from_url(url)[1])
            self.update_pages_to_be_crawled(page)
            yield page
        raise StopIteration


####################################################
# 1) what are the dead URLs 
def get_dead_pages(url, page_filter):
    crawl = Crawler(url, page_filter=page_filter)
    dead_urls = []
    for page in crawl:
        # just to see progress on the terminal
        print(crawl)
        print(page.http_code, page.url)
        
        # 2xx HTTP codes are for successful requests
        if not (200 <= page.http_code < 300):
            dead_urls.append((page.http_code, page.url))        
            
        source_pages = {}    
        for url in dead_urls:
            for source_page in crawl.pages_to_be_crawled_dict[url[1]]:
                if source_page in source_pages:
                    if url[0] in source_pages[source_page]:
                        source_pages[source_page][url[0]].append(url[1])
                    else:
                        source_pages[source_page][url[0]] = [url[1]]
                else:
                    source_pages[source_page] = {url[0]: [url[1]]}

    with open('dead_pages.txt', 'w') as dump_file:
        for source_page in source_pages:
            dump_file.write('Page contenant des liens defecteux : \n{}\n'
                        .format(source_page))
            dump_file.write('-'*70 + '\n')
            http_code = sorted(source_pages[source_page].keys())
            for code in http_code:
                dump_file.write('CODE HTTP {}\n'.format(code))
                for url in source_pages[source_page][code]:
                    dump_file.write('        {}\n'.format(url))
            dump_file.write('='*70 + '\n\n')

# 2) what are the less responsive pages
def get_slow_pages(url, page_filter):
    crawl = Crawler(url, page_filter=page_filter)
    pages_responsivness = []
    for page in crawl:
        # just to see progress on the terminal
        print(crawl)
        print(page.http_code, page.url)
        pages_responsivness.append((crawl.last_crawl_duration, page.url))

    pages_responsivness.sort(key=itemgetter(0), reverse=True)

    with open('slow_pages.txt', 'w') as dump_file:
        dump_file.write('Pages ordered from the slowest to the fastest\n')
        dump_file.write('-'*70 + '\n')
        for line in pages_responsivness:
            dump_file.write('{:.2f} seconds: {}\n'.format(line[0], line[1]))

if __name__ == '__main__':
    seed_url = 'http://www-sop.inria.fr/members/Arnaud.Legout/'
    page_filter = ['www-sop.inria.fr/members/Arnaud.Legout']
    get_dead_pages(seed_url, page_filter)
    #get_slow_pages(seed_url, page_filter)

    logging.shutdown()
