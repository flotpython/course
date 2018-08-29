# `nbautoeval`

`nbautoeval` is a very lightweight python framework for creating **auto-evaluated** exercises inside a jupyter (python) notebook.

Given a text that describes the expectations, students are invited to write
their own code,  and can then see the outcome on teacher-defined data samples,
compared with the results obtained through a teacher-provided solution, with a
visual feedback.

At this point, due to lack of knowledge/documentation about open/edx (read: the
version running at FUN), there is no available code for exporting the results as
grades or anything similar (hence the `autoeval` name).

There indeed are provisions in the code to accumulate statistics on all
attempted corrections, as an attempt to provide feedback to teachers.

# Try it on `mybinder`

Click the badge below to see a few sample demos under `mybinder.org` - it's all
in the `demo-notebooks` subdir.

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/parmentelat/nbautoeval)


# History

This was initially embedded into a [MOOC on python2](https://github.com/parmentelat/flotpython)
that ran for the first time on [the French FUN platform](https://www.france-universite-numerique-mooc.fr/)
in Fall 2014. It was then duplicated into a [MOOC on
bioinformatics](https://github.com/parmentelat/flotbioinfo) in Spring 2016
where it was named `nbautoeval` for the first time, but still embedded in a
greater git module.

The current git repo is created in June 2016 from that basis, with the intention
to be used as a git subtree from these 2 repos, and possibly others since a few
people have proved interested.

# Requirements

Target currently is any python-based notebook running on jupyter-v5. It is not
quite clear at this moment which version(s) specifically will work smoothly with
`nbautoeval`, but in essence there is very little dependency to the jupyter
version.

It was initially written in python2 but is now targetting primarily python3; hopefully it still works for python2 :)

# Installation

Initially, `nbautoeval` was used in MOOC courses, that in turn were implemented
as git repos; in this context `nbautoeval` was simply injected in this code
using git *subtree*.

It is now also available at pypi:

```
pip install nbautoeval
```

# Overview

In this early stage the framework supports the following types of exercises
  * `ExerciseFunction` : the student is asked to write a function
  * `ExerciseRegexp` : the student is asked to write a regular expression
  * `ExerciseClass` : tests will happen on a class implementation

A teacher who wishes to implement an exercise needs to write 2 parts :

* One python file that defines an instance of an exercise class. This in a nutshell typically involves
  * providing one solution (let's say a function) written in python
  * providing a set of input data
  * plus optionnally various tweaks for rendering the results

* One notebook that imports this exercise object, and can then take advantage of it to write jupyter cells that typically
  * invoke `example` on  the  exercise  object to show examples of the expected output
  * invite the student to write their own code
  * invoke `correction` on  the  exercise  object to display the outcome.

# Known issues

* there remains some hard-wired labels in French
* the regexp-based exercises come in too many variants and are thus not very well tested
