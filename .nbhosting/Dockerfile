# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/scipy-notebook

# NOTES for converting a Dockerfile from nbclassic
# - explicitly pip install jupyterlab-nbhosting
#   this is what does the menu customization
# - make sure to *NOT* install anything nb-classic
#   i.e. neither of
#   jupyter_contrib_nbextensions
#   jupyter-nbextensions-configurator
#   widgetsnbextension
# - nbhosting stock image now has fewer auto-installed libs
#   so make sure to pip install these if you actually need them
#   - ipywidgets
#   - nbautoeval
#   - ipythontutor

RUN true \
    # the crux of the matter
 && pip install jupyterlab-nbhosting \
    # formerly known as splitcell, used a lot \
 && pip install jupyterlab-gridwidth \
    # used only once to hide one code cell in taylor \
    # formerly known as hide_input \
 && pip install jupyterlab-hidecell \
    # auto-corrected exos \
 && pip install nbautoeval \
    # auto-illustrated examples \
 && pip install ipythontutor \
    # w7 comes with quite a few extra deps \
 && pip install plotly chart-studio  \
    # for the notebook on bokeh \
 && pip install bokeh jupyter-bokeh \
 && pip install jupyter-server-proxy \
    # for Taylor \
 && pip install autograd \
    # for Fourier \
 && pip install k3d \
    # section on pandas \
 && pip install seaborn \
    # w8 \
 && pip install aiohttp \
 && true
