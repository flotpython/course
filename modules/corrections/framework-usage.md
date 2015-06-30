#MOOC / framework / evoluations

## General case 

* mostly exos use the `ExerciceFunction` class

## regexps

* `W6/w6_regexp.py` uses the `ExerciceRegexp` and `ExerciceRegexpGroups` subclasses; input is not a function but some form of regexp string.

## others

There remains some other usages of `ExerciceFunction` that are not straightforward, makes sense to document them as they come up.

# reworking the framework

## Improve rendering:
check how to have full text of a truncated cell show up when hoverings

## ExerciceFunction

* should be mostly OK, but
  * would need to move to using rendering `Table*` objects 
  * once this is done we could decide to have some function exos (like the first ones chronologically) display the function name 

## ExerciceClass

* mostly working but
  * no support for column widths for now

