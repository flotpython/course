### Avoir un ipython avec fond blanc pour pouvoir faire une incrustation vid�o ###

* dans une fenetre GIT cmd, click droit sur la barre de titre et choisir "propri�t�s"
* Aller dans l'onglet Couleurs et choisir
   * Texte noir
   * Arri�re-plan blanc
   * Arri�re-plan (bo�te) blanc
   
   Tester la taille de la font avec Mathieu

* d�marrer ipython avec 
```
> ipython --profile mooc
```

J'ai cr�� un profile ipython pour le mooc avec
```
> ipython profile create
```

Et j'ai modifi� l'option `c.InteractiveShell.colors = 'LightBG'`

dans 
`C:\Users\alegout\.ipython\profile_mooc\ipython_config.py `
