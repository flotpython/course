Titre : Comment bien présenter votre code dans le forum


Bonjour à tous

Avant que le forum ne commence à s'animer, je voudrais attirer votre attention sur **la présentation, notamment des extraits de code**, dans le forum.

***

### Ce qu'il ne faut pas faire
Voici à quoi ressemble un morceau de code dans le forum **si je fais un simple copier-coller**.

**Si j'écris ceci**&nbsp;:

    def factoriel(n):
        if n <= 1:
            return 1
        else:
            return n*factoriel(n-1)

**Alors j'obtiens ceci**&nbsp;:

def factoriel(n):
    if n <= 1:
        return 1
    else:
        return n*factoriel(n-1)

***

### Ce qu'il faut faire

Comme vous allez vite le voir, en Python **les sauts de ligne sont très importants** ; c'est pourquoi il est crucial de présenter le code **comme vous le voyez vous-même**. 

**Si j'écris ceci**&nbsp;:

        def factoriel(n):
            if n <= 1:
                return 1
            else:
                return n*factoriel(n-1)

**Alors j'obtiens ceci**&nbsp;:


    def factoriel(n):
        if n <= 1:
            return 1
        else:
            return n*factoriel(n-1)


Ah, c'est déjà mieux. Et **pour obtenir ce résultat, c'est très simple**, je peux faire de plusieurs façons différentes :

 * Je sélectionne les 5 lignes de code ; juste au dessus de la zone où j'ai tapé le texte, il y a un petit menu, pour mettre en gras, en italique, etc.. Un des boutons a deux rangées de `0` et de `1`, c'est le symbole pour du code. Si je clique sur ce bouton avec mon code sélectionné, il se décale de 4 caractères vers la droite dans mon éditeur, et dans la fenêtre d'aperçu je vois que mon code est rendu correctement.

 * Pareil, mais au lieu d'appuyer sur le bouton `101` je fais Control-k (je suis sur mac, sur Windows j'imagine que ça sera sûrement Control-K ou Alt-K). C'est juste plus rapide. 

 * Je peux aussi insérer à la main les 4 espaces supplémentaires à gauche;  c'est fastidieux mais ça marche aussi

Tout ceci est valable aussi, naturellement, pour les messages d'erreur au terminal et autres contenus similaires.

***

### Pour aller plus loin 
Si vous voulez approfondir, le forum parle [un *markup* langage qui s'appelle `markdown`](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) (on est geek ou on ne l'est pas ;)). 

Notamment vous pouvez aussi pour peaufiner mettre les choses en gras, en italique, faire des listes à boulettes, etc...  Tout ceci est très bien, mais **en priorité** je vous incite à faire attention à ce que **votre code** soit lisible. Si vous ne présentez pas votre code correctement, surtout quand ça devient un peu long, on ne pourra pas vous comprendre.

***

### Vous pouvez aussi partager vos notebooks

Je signale enfin que, si vous souhaitez partager du code **que vous avez déjà écrit dans un notebook**, il existe une fonction créée spécialement pour cela, cherchez dans les menus la fonction "*Share static version*", qui vous donnera une URL pour **partager votre notebook en lecture seule** avec qui vous voulez. 

<br/>
Merci d'avance pour les autres élèves, et en attendant, donc, de lire votre code, bon MOOC à vous tous.
