# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/scipy-notebook

# we use splitcell a lot, so let's enable that extension
# to find out an extension's name
# look in the console in a jupyter that has it enabled
RUN jupyter nbextension enable splitcell/splitcell

# --------
# install plotly for w7
RUN pip install plotly==3.10.0

# for w7 as well
RUN pip install k3d
RUN pip install autograd

# nbautoeval is in the core images but we often need 
# the very latest version, that core images cannot
# always afford to follow very closely
RUN pip install -U nbautoeval

### speed up jupyter lab startup
RUN jupyter lab build
