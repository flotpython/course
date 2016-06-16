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

As of iteration 1, all exos used the `ExerciseFunction` class. Their implementation is sometimes a little twisted

* `from w2s3_slicing import exo_inconnue` - input is the string as computed by student, not a function

* `w6s6_regexp.py` uses the `ExerciseRegexp` and `ExerciseRegexpGroups` subclasses; input is not a function but some form of regexp string, that is turned into a function.

* ...

## Layouts

* default layout is `pprint` with columns `(24, 28, 28)`

* `multi_tri` : changes columns to (20, 20, 20)
* `multi_tri_reverse` : changes columns to (24, 24, 24)
* `decode_zen` 
  * hides call: `layout=void` at the Arg level (together with render_name=False, useful?)
  * `layout=text` at the exo level
  * layout_args=(None, 'x-small', 'x-small')

* `dispatch2`: chanes default columns to 50, 30, 30

* `comptage`
  * hides call : set `layout=void` at the Arg level
  * exo sets `layout=text_backslash_n`
  * layout_args=(None, 'x-small', 'x-small')

* `numbers` changes default columns to 30, 25, 25

The following need `truncate` because some args are function objects (add, mul, etc..) and we want these to show by **their names** and **not** the `<function ...>` string that `pprint` would give us otherwise

* `compare`, `compare_args`, `doubler_premier`  and `doubler_premier_kwds` use
  *  `layout=pprint` 
  *  `call_layout=truncate`
  *  `render_name=False`


