# `nbautoeval`

`nbautoeval` is a very lightweight python framework for creating **auto-evaluated** exercices inside a jupyter (python) notebook.

Given a text that describes the expectations, students are invited to write their own code, 
and can then see the outcome on teacher-defined data samples, compared with the results obtained through a teacher-provided solution, with a visual feedback.

At this point, due to lack of knowledge/documentation about open/edx (read: the version running at FUN), there is no available code for exporting the results as grades or anything similar (hence the `autoeval` name).

There indeed are provisions in the code to accumulate statistics on all attempted corrections, as an attempt to provide feedback to teachers.

# History

This was initially embedded into a [MOOC on python2](https://github.com/parmentelat/flotpython) 
that ran for the first time on [the French FUN platform](https://www.france-universite-numerique-mooc.fr/) in Fall 2014. 
It was then duplicated into a [MOOC on bioinformatics](https://github.com/parmentelat/flotbioinfo) 
in Spring 2016 where it was named `nbautoeval` for the first time, but still embedded in a greater git module.

The current git repo is created in June 2016 from that basis, with the intention to be used as a submodule from these 2 repos, 
and possibly others since a few people have proved interested.

# Requirements

Target currently is any python-based notebook running on jupyter-v4. It is not quite clear at this moment which version(s) 
specifically will work smoothly with `nbautoeval`, but in essence there is very little dependency to the jupyter version.

It was initially written in python2 but should be oblivious to a change of version to python3.

# Overview

In this early stage the framework supports the following types of exercices
  * `ExerciceFunction` : the student is asked to write a function
  * `ExerciceRegexp` : the student is asked to write a regular expression
  * `ExerciceClass` : tests will happen on a class implementation

A teacher who wishes to implement an exercice needs to write 2 parts :

* One python file that defines an instance of an exercice class. This in a nutshell typically involves
  * providing one solution (let's say a function) written in python
  * providing a set of input data
  * plus optionnally various tweaks for rendering the results

* One notebook that imports this exercice object, and can then take advantage of it to write jupyter cells that typically
  * invoke `exemple` on  the  exercice  object to show examples of the expected output
  * invite the student to write their own code
  * invoke `correction` on  the  exercice  object to display the outcome.

# Known issues

* Some terms are still phrased in French, like *exemple*, *exercice*, and similar.

