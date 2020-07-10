---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
notebookname: Gestion de sous-process
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Gestion de sous-process

+++

## Complément - niveau avancé

+++

Dans ce second notebook, nous allons étudier un deuxième programme Python, que j'appelle `game.py` (en fait c'est le présent notebook).

+++

### Fonctions de `game.py`

+++

Son travail va consister à faire plusieurs choses en même temps ; pour rester le plus simple possible, on va se contenter des trois fonctions suivantes :

* *scheduler* (chef d'orchestre) : on veut lancer à des moments préprogrammés des instances (sous-process) de `players.py` ;
* *multiplexer* (agrégateur) : on veut lire et imprimer au fur et à mesure les messages émis par les sous-processus ;
* horloge : on veut également afficher, chaque seconde, le temps écoulé depuis le début.

+++

En pratique, le programme `game.py` serait plutôt le serveur du jeu qui reçoit les mouvements de tous les joueurs, et diffuse ensuite en retour, en mode broadcast, un état du jeu à tous les participants.

+++

Mais dans notre version hyper simpliste, ça donne un comportement que j'ai essayé d'illustrer comme ceci :

+++

![](media/game.png)

+++

##### Remarque concernant les notebooks et le clavier

+++

Lorsqu'on exécute du code Python dans un notebook, les entrées clavier sont en fait interceptées par le navigateur Web ; du coup on ne peut pas facilement (du tout ?) faire tourner dans un notebook un programme asynchrone qui réagirait aussi aux événements de type entrée clavier.

C'est pour cette raison que le clavier apparaît sur ma figure en filigrane. Si vous allez jusqu'à **exécuter ce notebook localement** sur votre machine (voir plus bas), vous **pourrez utiliser le clavier** pour ajouter à la volée des éléments dans le scénario; il vous suffira de taper au clavier un numéro de 1 à 4 (suivi de *Entrée*) au moment où voulez **ajouter une paire de joueurs**, dans une des 4 configurations prédéfinies de `players.py`.

+++

##### Terminaison

+++

On choisit de terminer le programme `game.py` lorsque le dernier sous-processus `players.py` se termine.

+++

### Le programme `game.py`

+++

C'est ce notebook qui va jouer pour nous le rôle du programme `game.py`.

```{code-cell}
import asyncio
import sys
```

```{code-cell}
# cette constante est utile pour déclarer qu'on a l'intention
# de lire les sorties (stout et stderr)
# de nos sous-process par l'intermédiaire de pipes
from subprocess import PIPE
```

Commençons par la classe `Scheduler` ; c'est celle qui va se charger de lancer les sous-process selon un scénario configurable. Pour ne pas trop se compliquer la vie on choisit de représenter un scénario (un script) comme une liste de tuples de la forme :
```python
script = [ (time, predef), ...]
```
qui signifie de lancer, un délai de `time` secondes après le début du programme, le programme `players.py` dans la configuration `predef` - toujours de 1 à 4 donc.

```{code-cell}
class Scheduler:

    def __init__(self, script):

        # on trie le script par ordre chronologique
        self.script = list(script)
        self.script.sort(key = lambda time_predef : time_predef[0])

        # juste pour donner un numéro à chaque processus
        self.counter = 1
        # combien de processus sont actifs
        self.running = 0


    async def run(self):
        """
        fait tout le travail, c'est-à-dire :
        * lance tous les sous-processus à l'heure indiquée
        * et aussi en préambule, pour le mode avec clavier,
          arme une callback sur l'entrée standard
        """
        # pour le mode avec clavier (pas fonctionnel dans le notebook)
        # on arme une callback sur stdin
        asyncio.get_event_loop().add_reader(
            # il nous faut un file descriptor, pas un objet Python
            sys.stdin.fileno(),
            # la callback
            Scheduler.read_keyboard_line,
            # les arguments de la callback
            # cette fois c'est un objet Python
            self, sys.stdin
        )
        
        # le scénario prédéfini
        epoch = 0
        for tick, predef in self.script:
            # attendre le bon moment
            await asyncio.sleep(tick - epoch)
            # pour le prochain
            epoch = tick
            asyncio.ensure_future(self.fork_players(predef))


    async def fork_players(self, predef):
        """
        lance maintenant une instance de players.py avec cette config

        puis
        écoute à la fois sdtout et stderr, et les imprime
        (bon c'est vrai que players n'écrit rien sur stderr)
        attend la fin du sous-processus (avec wait())
        et retourne son code de retour (exitcode) du sous-processus

        par commodité on décide d'arrêter la boucle principale
        lorsqu'il n'y a plus aucun process actif
        """

        # la commande à lancer pour forker une instance de players.py
        # l'option python -u sert à désactiver le buffering sur stdout
        command = f"python3 -u data/players.py {predef}".split()
        
        # pour afficher un nom un peu plus parlant
        worker = f"ps#{self.counter} (predef {predef})"

        # housekeeping
        self.counter += 1
        self.running += 1

        # c'est là que ça se passe : on forke
        print(8 * '>', f"worker {worker}")
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=PIPE, stderr=PIPE,
        )
        # et on lit et écrit les canaux du sous-process
        stdout, stderr = await asyncio.gather(
            self.read_and_display(process.stdout, worker),
            self.read_and_display(process.stderr, worker))
        # qu'il ne faut pas oublier d'attendre pour que l'OS sache
        # qu'il peut nettoyer
        retcod = await process.wait()
        
        # le process est terminé
        self.running -= 1
        print(8 * '<', f"worker {worker} - exit code {retcod}"
              f" - {self.running} still running")
        
        # si c'était le dernier on sort de la boucle principale
        if self.running == 0:
            print("no process left - bye")
            asyncio.get_event_loop().stop()
        # sinon on retourne le code de retour
        return retcod


    async def read_and_display(self, stream, worker):
        """
        une coroutine pour afficher les sorties d'un canal
        stdout ou stderr d'un sous-process
        elle retourne lorsque le processus est terminé
        """
        while True:
            bytes = await stream.readline()
            # l'OS nous signale qu'on en a terminé
            # avec ce process en renvoyant ici un objet bytes vide
            if not bytes:
                break
                
            # bien qu'ici players n'écrit que de l'ASCII
            # readline() nous renvoie un objet `bytes`
            # qu'il faut convertir en str 
            line = bytes.decode().strip()
            print(8 * ' ', f"got `{line}` from {worker}")


    # ceci est seulement fonctionnel si vous exécutez
    # le programme localement sur votre ordinateur
    # car depuis un notebook le clavier est intercepté
    # par le serveur web
    def read_keyboard_line(self, stdin):
        """
        ceci est une callback; eh oui :)
        c'est pourquoi d'ailleurs ce n'est pas une coroutine
        cependant on est sûr qu'elle n'est appelée
        que lorsqu'il y a réellement quelque chose à lire
        """
        line = stdin.readline().strip()
        # ici je triche complètement
        # lorsqu'on est dans un notebook, pour bien faire
        # on ne devrait pas regarder stdin du tout
        # mais pour garder le code le plus simple possible
        # je choisis d'ignorer les lignes vides ici
        # comme ça mon code marche dans les deux cas
        if not line:
            return
        # on traduit la ligne tapée au clavier
        # en un entier entre 1 et 4
        try:
            predef = int(line)
            if not (1 <= predef <= 4):
                raise ValueError('entre 1 et 4')
        except Exception as e:
            print(f"{line} doit être entre 1 et 4 {type(e)} - {e}")
            return
        asyncio.ensure_future(self.fork_players(predef))
```

À ce stade on a déjà le cœur de la logique du *scheduler*, et aussi du multiplexer. Il ne nous manque plus que l'horloge :

```{code-cell}
class Clock:

    def __init__(self):
        self.clock_seconds = 0

    async def run(self):
        while True:
            print(f"clock = {self.clock_seconds:04d}s")
            await asyncio.sleep(1)
            self.clock_seconds += 1
```

Et enfin pour mettre tous ces morceaux en route il nous faut une boucle d'événements :

```{code-cell}
class Game:

    def __init__(self, script):
        self.script = script

    def mainloop(self):
        loop = asyncio.get_event_loop()

        # on met ensemble une clock et un scheduler
        clock = Clock()
        scheduler = Scheduler(self.script)

        # et on fait tourner le tout
        asyncio.ensure_future(clock.run())
        asyncio.ensure_future(scheduler.run())
        loop.run_forever()
```

Et maintenant je peux lancer une session simple ; pour ne pas être noyé par les sorties on va se contenter de lancer :

* 0.5 seconde après le début une instance de `players.py 1`
* 1 seconde après le début une instance de `players.py 2`

```{code-cell}
# nous allons juxtaposer 2 instances de players.py
# et donc avoir 4 joueurs dans le jeu
game = Game( [(0.5, 1), (1., 2)])
```

```{code-cell}
:latex:skip-eval: true
:tags: [raises-exception]

# si vous êtes dans un notebook
# cette exécution fonctionne, mais pour de sombres raisons
# liées à des évolutions de IPython, le kernel va mourir
# à la fin; ce n'est pas important..
game.mainloop()
```

### Conclusion

+++

Notre but avec cet exemple est de vous montrer, après les exemples des vidéos qui reposent en grande majorité sur `asyncio.sleep`, que la boucle d'événements de `asyncio` permet d'avoir accès, de manière simple et efficace, à des événements de niveau OS. Dans un complément précédent nous avions aperçu la gestion de requêtes HTTP ; ici nous avons illustré la gestion de sous-process.

Actuellement on peut trouver des bibliothèques au dessus de `asyncio` pour manipuler de cette façon quasiment tous les protocoles réseau, et autres accès à des bases de données.

+++

### Exécution en local

+++

Si vous voulez exécuter ce code localement sur votre machine :

Tout d'abord sachez que je n'ai pas du tout essayé ceci sur un OS Windows - et d'ailleurs ça m'intéresserait assez de savoir si ça fonctionne ou pas.

Cela étant dit, il vous suffit alors de télécharger le présent notebook au format Python. Vous aurez aussi besoin :

* [du code de `players.py`](data/players.py), évidemment ;
* et de modifier le fichier téléchargé pour lancer `players.py` au lieu de `data/players.py`, qui ne fait de sens probablement que sur le serveur de notebooks.

Comme on l'a indiqué plus haut, si vous l'exécutez en local vous pourrez cette fois interagir aussi via la clavier, et ajouter à la volée des sous-process qui n'étaient pas prévus initialement dans le scénario.

+++

## Pour aller plus loin

Je vous signale enfin, si vous êtes intéressés à creuser encore davantage, [ce tutorial intéressant qui implémente un jeu complet](https://7webpages.com/blog/writing-online-multiplayer-game-with-python-asyncio-getting-asynchronous/).

Naturellement ce tutorial est lui basé sur du code réseau et non, comme nous y sommes contraints, sur une architecture de type sous-process ; [le jeu en question est même en ligne ici](http://snakepit-game.com/)...
