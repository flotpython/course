flotpython
==========

# Purpose

This git repo contains the material for the MOOC 'Python : des fondamentaux à l'utilisation du langage' running on www.fun-mooc.fr

Both the python2 and python3 versions of that course are contained in this repo, although going back to python2 will require to travel back in time.

The actual videos that make the MOOC are not managed in this repository, only the preparation notes.

# Notebooks

Instead, and probably the most valuable contents, you will find here the notebooks used for illustrating the MOOC, together with all the required material.

## Infrastructure

As of 2017, we use the following app to host the notebook infrastructure when running the MOOC on FUN 

https://github.com/parmentelat/nbhosting

It's primarily a django app, running below an ngingx reverse proxy server, and spawning docker containers to isolate students in a sandbox where they can safely run their notebooks.


## How to run them

Here is a link to a binder instance, that in principle should be ready for playing with these notebooks online: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/parmentelat/flotpython)

Of course, you can also run them locally if you install jupyter locally.

We might also be able to give you access to the `nbhosting` instance, if you get in touch with us directly. 
