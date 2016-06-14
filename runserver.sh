#!/bin/bash

# just to be extra safe, let's set PYTHONPATH from the location of this script
# so that the demo notebooks will show up nicely

DIRNAME=$(dirname $0)
TOPLEVEL=$(cd $DIRNAME; pwd -P)

echo Using PYTHONPATH=$TOPLEVEL

PYTHONPATH=$TOPLEVEL jupyter-3.5 notebook-3.5
