#!/usr/bin/env python3

"""

pour des raisons techniques, il n'est pas possible de mettre en ligne
un notebook pour ce genre d'activités liées au réseau

ce bout de code est aussi proche que possible de l'exemple illustré
dans la vidéo, pour vous permettre de l'expérimenter de votre coté
en l'exécutant sur votre ordinateur

* lancé sans argument il reproduit l'expérience en mode asynchrone simple
  (cf. fetch)

* utilisez l'option -d (--details) pour utiliser fetch2, en montrant donc
  les lignes au fur et à mesure qu'elles arrivent

* utilisez l'option -s (--sequential) pour faire les accès en séquence

Vous pouvez utiliser une autre liste d'URLs en les passant sur la ligne de commande
e.g.:

$ async_http.py http://google.com http://facebook.com http://google.com http://facebook.com 

"""

##########
# contrairement au notebook, il nous faudra flusher les impressions
# sus sys.stdout, qui sinon sont bufferisées
import sys

import time


#################### la version séquentielle
import requests

def sequential(urls):
    for url in urls:
        req = requests.get(url)
        print(f"{url} returned {len(req.text)} chars")
    

#################### la version parallèle / asynchrone        
import asyncio
import aiohttp


# la première version, qui imprime simplement la fin de chaque url
async def fetch(url):
    
    async with aiohttp.ClientSession() as session:
        print(f"fetching {url}")
        
        async with session.get(url) as response:
            print(f"{url} response status {response.status}")
            raw = await response.read()
            print(f"{url} returned {len(raw)} bytes")


# la variante qui affiche toutes les lignes
async def fetch2(url, i):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url} response status {response.status}")
            # avec ici une itération asynchrone
            async for line in response.content: 
                print(f'{i}', end='')
                sys.stdout.flush()
    # dans la vidéo il y a ce return, c'est une différence
    # par rapport à la première variante mais ce n'est pas important
    return url


####################
# pour utiliser ce code directement depuis un terminal
import argparse


# ceci sera le défaut si vous ne précisez pas d'URL vous même:
default_urls = [
    "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs='*', 
                        default=default_urls,
                        help="URL's to be fetched")
    parser.add_argument("-s", "--sequential", default=False, action='store_true',
                        help="run sequentially")
    parser.add_argument("-d", "--details", default=False, action='store_true',
                        help="show details of lines as they show up (using fetch2)")
                        
    args = parser.parse_args()
    urls = args.urls

    loop = asyncio.get_event_loop()

    # mode séquentiel
    if args.sequential:
        print(f"Running sequential mode on {len(urls)} URLs")
        beg = time.time()
        sequential(urls)
        print(f"duration = {time.time()-beg}s")

    # mode asynchrone
    else:
        
        # sans option on utilise juste fetch
        if (not args.details):
            print(f"Running simple mode (fetch) on {len(urls)} URLs")
            jobs = (fetch(url) for url in urls)
        else:
            print(f"Running detail mode (fetch2) on {len(urls)} URLs")
            jobs = (fetch2(url, i) for i, url in enumerate(urls))
        # il n'y a plus qu'à
        beg = time.time()
        loop.run_until_complete(asyncio.gather(*jobs))
        print(f"duration = {time.time()-beg}s")


if __name__ == '__main__':
    main()
