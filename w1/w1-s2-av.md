Après la vidéo sur l'organisation du
cours et avant notre premier contact
avec la technique, je vais vous
expliquer pourquoi python est un langage
très agréable à utiliser, et qui se
prête à peu près à toutes les
applications.

python est un langage qui a tout un tas
de bonnes propriétés, et parmi elles la
plus frappante, il me semble, est que
c'est un langage très lisible.

========== lisible (1)

Je vais essayer de vous en convaincre
avec quelques petits
exemples où je compare python avec
d'autres langages généralistes.

========== fragment code C++

Je commence avec C++; bon tous ces
exemples sont uniquement à titre
indicatif, je ne voudrais pas non plus
déclencher une avalanche sur le forum, je
veux simplement illustrer mon propos.

Donc voici la forme générale d'un
parcours de liste en C++, disons
traditionnel.

========== fragment code python

En python la même chose ressemble à
cela.

La première chose qu'on voit c'est que
c'est beaucoup moins touffu; en python
il n'y a presque pas de ce qu'on appelle
le sucre syntaxique, c'est-à-dire pas
d'accolades, de point-virgules ou autres
begin/end, la syntaxe repose uniquement
sur la présentation.

Ici vous voyez par exemple que les
appels a `print()` et a `manage()` ont la
même indentation, ça suffit pour que un
humain voie immédiatement la logique, et
c'est aussi comme ça que marche le langage.

Ça rend le code plus facile à lire,
parce tout simplement il y a moins de
bruit visuellement, et en plus bien sûr
ça prend moins de place.

========== lisible(2)

Regardons maintenant java. Ici c'est le
traditionnel programme "hello world",
qui bien sûr écrit juste hello world.

========== fragment code python 

En python c'est bien plus court, ça se
résume à une ligne.

Bon j'admets que j'ai choisi un exemple
pathologique, mais j'aime bien le
montrer parce que ça illustre un autre
point qui me semble important.

Si il y a une telle disproportion entre
les deux, c'est un peu lié à la syntaxe,
mais c'est aussi et surtout parce que
java a une approche dogmatique, qui dit
que tout doit être dans une classe; et
ça me pénalise dans ce cas où je veux
juste écrire un programme ultra simple.

========== lisible (3)

Regardons encore pour finir javascript,
j'ai pris cette fois un exemple
classique de programmation
fonctionnelle, on veut calculer la liste
des carrés des nombres dans une liste.

========== fragment code python 

en python ça donne ceci

ici encore vous voyez que la version
python est plus dépouillée, ce qui la
rend, à mon avis, plus
expressive et plus facile à lire.

Bon à nouveau, j'admets volontiers que
le choix des exemples est très
arbitraire, je voulais mettre en
évidence deux points qui me semblent
essentiels.

========== traits dominants

Le premier, c'est que la facilité
d'accès est considéré comme un but.

========== fragment facilité d'accès

Un code plus facile à lire, ça veut dire
d'abord qu'on va pouvoir plus facilement
travailler avec des gens, qui vont plus
vite comprendre de quoi il retourne.

Quand je dis facilité d'accès, ça veut
aussi dire avoir une approche cognitive,
et se demander dans tous les choix de
conception du langage si telle ou telle
solution permet d'éviter les confusions
et les malentendus.

Bref, mon point c'est que si python est
agréable à lire, ce n'est pas arrivé par
hasard, c'est vraiment un objectif
central et cela depuis le tout début.


La syntaxe, ça peut paraître un détail;
mais j'ai choisi de commencer
par vous montrer ça parce c'est très
révélateur de l'état d'esprit dans
lequel le langage est concu et continue
d'évoluer.

========== fragment 

Et c'est le deuxième trait sur lequel je
voulais attirer votre attention.
Par opposition à ce que
disais tout à l'heure à propos de java,
en python il n'y a pas de dogme, les
choix sont guidés par le pragmatisme.

Ce que je veux dire, c'est que par
exemple le choix de cette syntaxe
orientée indentation, c'est quelque
chose de très peu académique, on l'a vu
sur les bouts de code de tout à l'heure.

Mais comme on a considéré que ça en
valait la peine, on a cassé les codes
pour arriver à le faire, et il se trouve
qu'en effet ça marche. Il y a dans
python plein d'autres innovations qui
sont arrivées exactement de la même
façon, les mécanismes d'itération par
exemple; et quand on décide d'intégrer
une nouveauté dans le langage, parce
qu'on trouve que ça répond à un besoin
important dans la pratique, tous les
moyens sont bons

========== historique

Sans transition voici rapidement
l'historique des versions du langage, ça
vous étonnera peut-être mais python est
un langage assez ancien déjà, puisque la
première version a presque 25 ans. Bon
inutile de vous dire que cette version
du langage n'avait pas grand-chose à
voir avec python-3.6.

========== fragment

Comme vous le savez sans doute, il y a
eu une seule rupture de
compatibilité au moment de
l'introduction de python3. Ça a été
assez douloureux, on est tous d'accord,
mais d'un autre coté c'était nécessaire
car on ne pouvait pas continuer avec
cette idée qu'un caractère ça tient sur
un octet.

[AL: tu est sûr que 2.0 pouvait 
faire tourner du code 1.5?]]

Et si vous regardez les autres langages,
une seule rupture de compatibilité en
près de 25 ans c'est peu.

========== stabilité

Ce qui m'amène à évoquer une autre bonne
propriété de python, sa stabilité.

Je ne m'appesantis pas, bien entendu un
langage aussi utilisé se doit de
garantir que le code qu'on écrit
aujourd'hui tournera toujours demain ou
après-demain, c'est le cas bien sûr ici.

========== fragment 2.7 .. 2020

Par exemple pour donner une idée,
lorsque python3 a été releasé fin 2008,
comme le code n'était plus compatible,
python2 a été d'abord maintenu jusque
2015, puis ça a été étendu jusque
2020, ça fait quand même en tout presque
12 ans.

========== fragment librairie standard

Ça me donne l'occasion de vous parler de
la librairie standard; la librairie
standard, c'est l'ensemble des
utilitaires qui sont **installés avec le
langage** à proprement parler. 

Elle fait partie du **même package logiciel**, 
du coup elle est **maintenue indéfiniment**
 - en tous cas autant que le langage lui-même
 - c'est ce qui fait la différence
principale avec d'autres librairies
tierces, il faut s'en souvenir si la
stabilité à long terme est une
préoccupation pour vous.

========== slide portable

Je signale aussi rapidement que python
est portable, ça veut dire que le même
code va marcher sur windows, linux et
mac sans modification. C'est un atout
appréciable, même si de nos jours ce
n'est pas très discriminant.
[[AL: un mot sur raspberryPi?]]

========== très grosse base de code

Sinon vous pouvez trouver en quelques
clics une librairie pour faire à peu
près tout; il y a bien sûr les gros
joueurs pour le calcul scientifique 

--- fragments ...

et
le traitement de données, et tout ce qui
est services web, mais au-delà de ça si
on est pressé on trouve vraiment tout ce
qu'on veut.

========== 2eme slide "très grosse base de code"

Et pour répondre à une critique que
j'entends souvent par rapport à la
performance en python, je précise aussi
qu'il est relativement facile de prendre
du code natif écrit en C ou en C++, et
de l'enrober dans une interface python.

Et c'est fréquemment le cas pour les
librairies qui ont besoin de cycles.
Clairement si la performance était un
problème rédhibitoire, on ne verrait
sûrement pas tant de gens faire de la
data science en python.

========== développement rapide

Donc on a un langage facile à lire, avec
énormément de librairies disponibles
dans la nature.

Si vous ajoutez à ça:

========== fragment  
des types de base super puissants et
très efficaces, notamment ceux basés sur
les tables de hachage, et en plus les tableaux numpy

========== fragment
la gestion de la mémoire qui est faite
pour vous avec un garbage collector,

========== fragment
le fait que le langage est interprété,
avec comme commodité supplémentaire les
notebooks jupyter, je vous montrerai ça
très bientôt,

Eh bien ça vous donne un rythme de
développement très rapide.

Alors c'est vrai qu'en toute généralité,
si vous ne faite pas spécialement
attention, un programme python va être
moins performant qu'un programme C ou
Java. Mais bon d'un autre coté vous
allez l'écrire beaucoup plus vite;
est-ce que vous préfèrez économiser les
cycles processeur ou votre temps à vous?

En plus à nouveau, il y a des tas de
moyens d'arriver à des performances tout
à fait honorables lorsque ça devient un
souci.


========== licence très flexible

Je finirai en vous disant un mot de la
licence et de la gouvernance.

Les droits sont détenus par la PSF -
python software foundation, qui est une
organisation communautaire et non
lucrative. La licence d'utilisation
elle-même est très flexible et vous
permet essentiellement d'écrire ce que
vous voulez, que ce soit à des fins
commerciales ou non.

========== évolutions

Enfin pour dire un mot de la prise de
décisions concernant les évolutions du langage:

ça va peut vous étonner mais en
fait il se passe encore beaucoup de
choses dans la communauté python, on
verra ça par exemple dans le module
optionnel sur la programmation
asynchrone qui est très très innovante.

========== fragment débat démocratique

Les débats concernant les évolutions
sont bien sûr totalement démocratiques,

========== fragment BDFL

par contre la décision finale revient en
dernier ressort au créateur du langage,
Guido van Rossum qui s'est baptisé
lui-même le BDFL pour dictateur bénévole
pour la vie.

Ça a je pense contribué jusqu'ici à donner une
bonne cohérence dans le langage.

========== popularité

Voilà j'espère vous avoir convaincu que
vous avez fait un bon choix en décidant
d'apprendre python

D'ici la prochaine vidéo vous aurez
besoin d'installer python puisque nous
allons commencer à maniper un peu, donc
à nouveau j'attire votre attention sur
les compléments où nous vous donnons
quelques indications pour faire ça

à bientôt

