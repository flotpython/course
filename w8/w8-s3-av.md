# w8-s3

## Résumé de la vidéo

Nous avons vu quelques exemples simples
de programmation asynchrone avec
asyncio. Dans cette séquence, après un
rapide historique nous allons maintenant
voir quelles sont les librairies
disponibles pour tirer profit de ce
nouveau paradigme

# historique

========== [fragment 3.5]

Dans sa forme actuelle avec 'async def'
et 'await', la syntaxe date de
python-3.5, en 2015 donc. Je vous
signale rapidement que asyncio avait en
fait été introduite un an plus tôt dans
python-3.4,

========== [fragment 3,4]

mais avec une syntaxe différente, que je
vous montre ici rapidement, il se peut
que vous trouviez du code avec cette
ancienne syntaxe.

========== [slide python-2]

enfin il faut savoir que les mécanismes
dont on a besoin pour implémenter une
boucle d'événements sont présents dans
le langage depuis déjà python-2.5 c'est
à dire 2006.

je vous signale d'ailleurs plusieurs
projets qui ont tiré profit de cette
possibilité, qui sont

========== [slide 'inspiration']

gevent, tornado et twisted, qui
utilisent une technologie similaire
depuis bien avant asyncio, et qui
d'ailleurs l'ont largement inspiré.

à cet égard, s'il est fréquent de
résumer ce style de programmation sous
le simple nom de 'asyncio', il est sans
doute utile aussi de bien distinguer
entre les traits qui appartiennent au
langage - qui sont donc par définition
peu flexibles - de ceux qui sont
implémentées dans la librairie.

========== [slide langage vs librairie (1)]

La distinction est assez nette, le
langage contient principalement

========== [fragment]

la notion de coroutine, qui se
matérialise avec les mots clés `async
def` et `await`,

et quelques produits dérivés comme
`async for` et `async with` que l'on
aura l'occasion de voir plus tard

========== [slide langage vs librairie (2)]

La librairie quant à elle implémente
principalement la boucle d'événements.

========== [fragment]

C'est important de comprendre la
distinction, car cela signifie qu'il est
tout à fait possible d'envisager
d'autres librairies asynchrones qui
partagent toutes le même modèle de
coroutines, et qui coexistent. Les trois
projets que j'ai cités tout à l'heure
peuvent par exemple continuer à utiliser
leurs propres librairies, mais avec une
façon plus simple et plus standard
d'écrire leurs coroutines que ce qu'ils
avaient pu écrire en 2010.

Outre la boucle d'événements, on trouve
aussi dans asyncio, un peu en vrac:

========== [fragment]

Des objets de base pour la
synchronisation, comme les classes
`Queue` `Lock` et `Semaphore`

========== [fragment]

un package Subprocess pour l'interaction
avec les processus, la version
asynchrone de la librairie standard
'subprocess'

========== [fragment]

et enfin des abstractions, qu'on peut
voir si on veut comme des frameworks -
ou des design patterns - pour
l'implémentation de comportements plus
évolués, comme les notions de transport
et de protocole, pour l'implémentation
par exemple d'une pile http.

Nous avons déjà un peu rencontré les
coroutines, et la boucle d'événements
pour faire tourner nos premiers exemples
dans la précédente vidéo. Pour le reste,
à nouveau, il ne sera pas question de
couvrir exhaustivement tous ces sujets,
mais nous verrons d'autres exemples de
tout ça dans les prochaines vidéos.


Pour l'instant, je voudrais vous donner
quelques généralités à propos de ce
paradigme.

========== [slide utilisable en prod ?]

Tout d'abord, à l'heure où je vous parle
en 2017, asyncio fait partie intégrante
de la librairie standard, et non plus à
titre expérimental comme c'était le cas
avec la 3.5. Ça veut dire donc qu'elle
sera maintenue et supportée pour de
nombreuses années.

Même si on a encore relativement peu
d'expérience - 2 ans à cette échelle, ça
en fait une technologie très récente -
il y a clairement un consensus sur le
fait que cette approche apporte quelque
chose et qu'il est extrêmement
intéressant de voir jusqu'où on peut
aller.  Ne serait-ce qu'en terme
d'échelle, il est admis qu'à ressources
constantes, on peut heberger plus
d'acteurs concurrents qu'avec des
threads, et donc à priori qu'avec des
processus, dans un rapport de plusieurs
ordres de grandeur - au moins 100.

À savoir également, il y a aujourd'hui
une offre très complète

========== [fragments]

notamment tous les protocoles réseau les
plus populaires, les drivers de base de
données, essentiellement tout est
disponible dans une forme compatible
avec ce paradigme.

Donc si on me demande si cette
technologie est utilisable en
production, je réponds oui. Cela dit..

========== [slide Mais..]

il y a des mais, des incertitudes. 

Maintenant, il y a des incertitudes; une
des choses à remarquer pour commencer,

========== [fragment]

c'est le coté très contagieux des
coroutines; dès qu'on se met à utiliser
asyncio, on se retrouve à avoir envie
d'une version asynchrone pour .. à peu
près tout.

Et comme on a fait le choix que les
changements de contexte sont explicites
avec await - il faut récrire le code
pour tirer profit de ce modèle de
programmation. Mais bon, comme on vient
de le voir, cela n'est pas un souci,
l'écosystème est très complet.

L'autre incertitude que je voulais
signaler pour terminer, c'est que le
consensus n'est pas total sur les choix
faits dans la librairie asyncio. Tout
le monde est d'accord sur le concept de
coroutine, mais je signale tout de même
quelques travaux très intéressants

========== [fragment]

qui visent à en tirer un meilleur
profit, et qui pourraient bien
influencer une version 2 de asyncio dans
le futur.

Bon même si ça devait arriver,
rassurez-vous, ce qu'on
va apprendre sur la syntaxe, les coroutines, les
awaitables, et de façon plus générale le
modèle mental restera valable.


Tout ceci étant dit, nous allons en
rester là pour les généralités, on se
retrouve dans la prochaine vidéo pour un
peu de vrai code.

À bientôt
