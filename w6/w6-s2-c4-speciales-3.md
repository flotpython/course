---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
nbhosting:
  title: "M\xE9thodes sp\xE9ciales (3/3)"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Méthodes spéciales (3/3)

+++

## Complément - niveau avancé

+++

Ce complément termine la série sur les méthodes spéciales.

+++

### `__getattr__` et apparentés

+++

Dans cette dernière partie nous allons voir comment avec la méthode `__getattr__`, on peut redéfinir la façon que le langage a d'évaluer :

```python
objet.attribut
```

+++

**Avertissement :** on a vu dans la séquence consacrée à l'héritage que, pour l'essentiel, le mécanisme d'héritage repose **précisément** sur la façon d'évaluer les attributs d'un objet, aussi nous vous recommandons d'utiliser ce trait avec précaution, car il vous donne la possibilité de "faire muter le langage" comme on dit.

+++

**Remarque :** on verra en toute dernière semaine que `__getattr__` est *une* façon d'agir sur la façon dont le langage opère les accès aux attributs. Sachez qu'en réalité, le protocole d'accès aux attributs peut être modifié beaucoup plus profondément si nécessaire.

+++

##### Un exemple : la classe `RPCProxy`

+++

Pour illustrer `__getattr__`, nous allons considérer le problème suivant. Une application utilise un service distant, avec laquelle elle interagit au travers d'une API.

C'est une situation très fréquente : lorsqu'on utilise un service météo, ou de géolocalisation, ou de réservation, le prestataire vous propose une **API** (Application Programming Interface) qui se présente bien souvent comme une **liste de fonctions**, que votre fonction peut appeler à distance au travers d'un mécanisme de **RPC** (Remote Procedure Call).

Imaginez pour fixer les idées que vous utilisez un service de réservation de ressources dans un Cloud, qui vous permet d'appeler les fonctions suivantes :

 * `GetNodes`(...) pour obtenir des informations sur les noeuds disponibles ;
 * `BookNode`(...) pour réserver un noeud ;
 * `ReleaseNode`(...) pour abandonner un noeud.

+++

Naturellement ceci est une API extrêmement simplifiée. Le point que nous voulons illustrer ici est que le dialogue avec le service distant :

 * requiert ses propres données - comme l'URL où on peut joindre le service, et les identifiants à utiliser pour s'authentifier ;
 * et possède sa propre logique - dans le cas d'une authentification par session par exemple, il faut s'authentifier une première fois avec un login/password, pour obtenir une session qu'on peut utiliser dans les appels suivants.

+++

Pour ces raisons il est naturel de concevoir une classe `RPCProxy` dans laquelle on va rassembler à la fois ces données et cette logique, pour soulager toute l'application de ces détails, comme on l'a illustré ci-dessous :

<img src="media/rpcproxy.png">

+++

Pour implémenter la plomberie liée à RPC, à l'encodage et décodage des données, et qui sera interne à la classe `RPCProxy`, on pourra en vraie grandeur utiliser des outils comme :

 * [`xmlrpc.client`](https://docs.python.org/3/library/xmlrpc.client.html) qui fait partie de la bibliothèque standard ; 
 * ou, pour JSON, une des nombreuses implémentations qu'un moteur de recherche vous exposera si vous cherchez `python rpc json`, comme par exemple [`json-rpc`](https://pypi.python.org/pypi/json-rpc/).

Cela n'est toutefois pas notre sujet ici, et nous nous contenterons, dans notre code simplifié, d'imprimer un message.

+++

##### Une approche naïve

+++

Se pose donc la question de savoir quelle interface la classe `RPCProxy` doit offrir au reste du monde. Dans une première version naïve on pourrait écrire quelque chose comme :

```{code-cell} ipython3
# la version naïve de la classe RPCProxy

class RPCProxy:
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def _forward_call(self, functionname, *args):
        """
        helper method that marshalls and forwards 
        the function and arguments to the remote end
        """
        print(f"""Envoi à {self.url}
de la fonction {functionname} -- args= {args}""")
        return "retour de la fonction " + functionname
    
    def GetNodes (self, *args):
        return self._forward_call ('GetNodes', *args)
    def BookNode (self, *args):
        return self._forward_call ('BookNode', *args)
    def ReleaseNode (self, *args):
        return self._forward_call ('ReleaseNode', *args)
```

Ainsi l'application utilise la classe de cette façon :

```{code-cell} ipython3
# création d'une instance de RPCProxy

rpc_proxy = RPCProxy(url='http://cloud.provider.com/JSONAPI', 
                     login='dupont',
                     password='***')

# cette partie du code, en tant qu'utilisateur de l'API, 
# est supposée connaître les détails
# des arguments à passer 
# et de comment utiliser les valeurs de retour
nodes_list = rpc_proxy.GetNodes ( 
    [ ('phy_mem', '>=', '32G') ] )

# réserver un noeud
node_lease = rpc_proxy.BookNode (
    { 'id' : 1002, 'phy_mem' : '32G' } )
```

##### Discussion

+++

Quelques commentaires en vrac au sujet de cette approche :

* l'interface est correcte ; l'objet `rcp_proxy` se comporte bien comme un proxy, on a donné au programmeur l'illusion complète qu'il utilise une classe locale (sauf pour les performances bien entendu...) ;
* la séparation des rôles est raisonnable également, la classe RPCProxy n'a pas à connaître le détail de la signature de chaque méthode, charge à l'appelant d'utiliser l'API correctement ;
* par contre ce qui cloche, c'est que l'implémentation de la classe RPCProxy dépend de la liste des fonctions exposées par l'API ; imaginez une API avec 100 ou 200 méthodes, cela donne une dépendance assez forte et surtout inutile ;
* enfin, nous avons escamoté la nécessité de faire de RPCProxy un [singleton](http://en.wikipedia.org/wiki/Singleton_pattern), mais c'est une toute autre histoire.

+++

##### Une approche plus subtile

+++

Pour obtenir une implémentation qui conserve toutes les qualités de la version naïve, mais sans la nécessité de définir une à une toutes les fonctions de l'API, on peut tirer profit de `__getattr__`, comme dans cette deuxième version :

```{code-cell} ipython3
# une deuxième implémentation de RPCProxy

class RPCProxy:
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def __getattr__(self, function):
        """
        Crée à la volée une méthode sur RPCProxy qui correspond
        à la fonction distante 'function'
        """
        def forwarder(*args):
            print(f"Envoi à {self.url}...")
            print(f"de la fonction {function} -- args= {args}")
            return "retour de la fonction " + function
        return forwarder
```

Qui est cette fois **totalement découplée** des détails de l'API, et qu'on peut utiliser exactement comme tout à l'heure :

```{code-cell} ipython3
# création d'une instance de RPCProxy

rpc_proxy = RPCProxy (url='http://cloud.provider.com/JSONAPI', 
                      login='dupont',
                      password='***')

# cette partie du code, en tant qu'utilisateur de l'API, 
# est supposée connaître les détails
# des arguments à passer 
# et de comment utiliser les valeurs de retour
nodes_list = rpc_proxy.GetNodes ( 
    [ ('phy_mem', '>=', '32G') ] )

# réserver un noeud
node_lease = rpc_proxy.BookNode (
    { 'id' : 1002, 'phy_mem' : '32G' } )
```
