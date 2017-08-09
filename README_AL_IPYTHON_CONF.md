### Avoir un ipython avec fond blanc pour pouvoir faire une incrustation vidéo ###

* dans une fenetre GIT cmd, click droit sur la barre de titre et choisir "propriétés"
* Aller dans l'onglet Couleurs et choisir
   * Texte noir
   * Arrière-plan blanc
   * Arrière-plan (boîte) blanc

* démarrer ipython avec 
```
> ipython --profile mooc
```

J'ai créé un profile ipython pour le mooc avec
```
> ipython profile create
```

Et j'ai modifié l'option `c.InteractiveShell.colors = 'LightBG'`

dans 
`C:\Users\alegout\.ipython\profile_mooc\ipython_config.py `
