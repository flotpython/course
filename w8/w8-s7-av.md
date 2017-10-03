# w8-s7
## Résumé de la vidéo

. tâche
. pile, variables
. résultat traitement
. exceptions

[[AL: commentaire global pour cette vidéo. Ça me semble un gros pas en
avant et je pense que cette vidéo pourrait venir plus tard. Tu parles
de Task en introduisant très/trop rapidement cette notion et de yield
(c'est encore await dans le texte) sans avoir expliqué avant que await
fait en fait de la délégation, mais ne rend pas la main à la boucle,
c'est un yield dans une coroutine qui rend la main (même si ce yield
est caché dans la librairie asynchrone). ]]

[[TP: tu as raison, je pense ajouter une
  première animation pour expliquer les
  appels à partir d'une coroutine, les
  empilements, et le yield
  ça va peut-être tout décaler un peu
  mais bon..
  ]]


Maintenant que nous avons vu comment
créer et utiliser une une boucle
d'événements, nous allons entrer un peu
plus dans le détail, et parler des
tâches.

On va voir ça dans une animation:

* qui va je l'espère bien vous faire
comprendre comment se passe un programme
asynchrone,

* et où on va voir comment se passe la
gestion des exceptions

C'est une vision très simplifiée de la
réalité mais j'espère que ça éclaircira
un peu les choses. 

========== cliquer sur Animation
[[pour revenir en arrière dans
l'animation, faire Shift-left]]

Donc on part d'une boucle dans laquelle
[click]
on ajoute des coroutines avec
ensure_future.
[click]
la boucle crée en interne un objet de
type Task pour wrapper la coroutine

4 x [click]

ici j'ajoute trois coroutines, ça me
fait 3 tâches.

Une fois que j'ai rempli ma boucle
d'événements, je lance ma boucle;

[click - run_forever() apparait]

la première chose qu'elle va faire ça va
être de choisir une de ses tâches et de
lancer l'évaluation de la coroutine.

[click tâche courante]

Comme les coroutines peuvent s'appeler
les unes les autres, le lancement de la
coroutine en question se fait dans une
pile d'appels dédiée. 

[click]

Si vous vous souvenez ce qu'on a dit en
introduction, c'est conceptuellement
exactement comme un thread, on a une
pile par tâche - sauf qu'ici c'est la
boucle qui va contrôler la commutation
de contexte et pas l'OS.

[click]

La boucle laisse la main à cette tâche
jusqu'à ce qu'on atteigne un await qui
corresponde à un futur; jusqu'ici on n'a
vu principalement que asyncio.sleep,
mais la boucle fournit des mécanismes de
base sur les connections, les process,
et ce genre de choses.

Bref au moment où la tâche ne peut plus
continuer, que je représente par await
ici
[click montrer await]

la boucle reprend le contrôle et choisit
une autre tâche à faire avancer

c'est important de noter que la pile de
la première tâche est conservée quelque
part; sinon on ne pourrait pas reprendre
le traitement plus tard, car la pile
contient naturellement les variables qui
sont le contexte de la tache

[click move to 2eme tache]

Donc après avoir sauvegardé la pile on
passe le contrôle à la coroutine dans la
deuxieme tache, donc comme tout à
l'heure

[clics multiples jusque await]

ou on détecte un point d'attente, on
passe par exemple à la troisième tache

[click]

qui elle aussi travaille

[clicks multiples:
tache3 ..
tache1 avance d'un cran
retour à la tache 3
]

Bon, maintenant voyons comment ça se
termine; dans le cas simple ou la
coroutine ne lève pas d'exception, voici
ce que fait la boucle

[click enlever await]
[click depiler]
[click depiler]

lorsque le dernier frame retourne un
résultat, la boucle le range dans la 
tache et marque la tache comme terminée.

[click result() & opacity]

et on repasse la main à une autre tache

[click -> sel. tache 2]

====================
Voyons maintenant le cas où une
exception est levée; ici deux cas se
présentent.

Le plus simple d'abord, c'est le cas où
l'exception est attrapée dans cette
pile-là

[click x 2 : raise au lieu de await]

vous vous souvenez ce qu'on a dit sur le
traitement des exceptions, c'est pareil
ici, à partir du raise on cherche dans
la pile un try: qui attrape
l'exception. Ici je suppose que j'en
trouve un à l'intérieur de la tache 2.

[click x 2]

dans ce cas là c'est très simple, on
fait exactement comme dans du code
synchrone, et on continue comme si de
rien n'était.

[click ... select. tache 1]

==========
Maintenant si on *n'a PAS* attrapé
l'exception dans cette pile.

la tache 1 leve une exception mais on ne
trouve pas de handler dans cette pile.

[click jusqu'à voir <--- raise]

Alors ce que va faire la boucle
typiquement c'est d'attraper
l'exception, de la conserver

[click 2x exception()]

dans l'objet Task comme on avait
conservé le résultat tout a l'heure,
et de marquer la tache comme terminée.


========== [fermer animation Command w]
========== [retour notebook]
========== [slide bonnes pratiques]

Ceci nous permet de conclure avec une
bonne pratique concernant les exceptions

========== [fragment]
* Tout d'abord je vous conseille
d'attraper autant que possible les
exceptions à l'intérieur du code
asynchrone

* Ensuite pour les autres cas, on verra
  dans une autre séquence que vous êtes
  encouragés à lire les exceptions
  attachées aux tâches; pour cela il
  suffit d'appeler la méthode
  exception() sur l'objet Task.



