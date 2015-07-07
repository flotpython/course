# MOOC exos

## validation

Running 

    cd corriges
    make validation
    
will create a notebook `modules/corrections/validation.ipynb` that has all the exos present with a sample of the correction layout.

To visualize this

    cd modules/corrections
    f2
    
## Known exceptions

At this point, `make validation` will issue

* 2 pairs of warning messages about `liste_racines` and `affichage` that are deprecated exos (but still in the corrections for now)

* 2 current exos that could not fit the validation framework:
  * `from corrections.w5s6_rpcproxy`
  * `from data.shipdict import Position, Ship, ShipDict`

None of these 2 are really online-corrected; they do make it to the 'corriges/' and that is the only reason why they are mentioned here.

## Lower-level exceptions 

As of iteration 1, all exos used the `ExerciceFunction` class. Their implementation is sometimes a little twisted

* `from w2s3_slicing import exo_inconnue` - input is the string as computed by student, not a function

* `w6s6_regexp.py` uses the `ExerciceRegexp` and `ExerciceRegexpGroups` subclasses; input is not a function but some form of regexp string, that is turned into a function.







There remains some other usages of `ExerciceFunction` that are not straightforward, makes sense to document them as they come up.


