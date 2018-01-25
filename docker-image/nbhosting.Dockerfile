# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM jupyter/scipy-notebook:latest
# at some point we were specifying a fixed version
# FROM jupyter/scipy-notebook@sha256:d6ebaf357aa9cbc20aa8982b1860a454b90aa599377999212e2889ab5f764aea
# in particular in oct. 2017 when using latest
# we had header-container still visible when the notebooks showed up
# however this was fixed with commit 978156d63b0afd26fb130a18017adccf3cb77332
# see also https://github.com/jupyter/docker-stacks/issues/480#issuecomment-336603502


# --------
# for interfacing with nbhosting, we need this startup script in all images
# and we need to be root again for installing stuff
USER root
COPY start-in-dir-as-uid.sh /usr/local/bin

# this is to increase the ulimit -n (max nb of open files)
# as perceived by regular user processes in the container 
# before we implement this setting, default was 1024
# 128 * 1024 looks about right
# container root was OK at 1024*1024
RUN for type in hard soft; do echo '*' $type nofile 131072 ; done > /etc/security/limits.d/open-file.conf

# add lsof in the mix to help troubleshoot shortages of open files
RUN apt-get update && apt-get install lsof

# --------
# hacks for jupyter itself
# (*) disable check done when saving files - see https://github.com/jupyter/notebook/issues/484
# (*) disable the 'Trusted' notification widget
RUN (find /opt /usr -name notebook.js -o -name main.min.js | xargs sed -i -e 's|if (check_last_modified)|if (false)|') \
 &&  (find /opt /usr -name notificationarea.js -o -name main.min.js | xargs sed -i -e 's|this.init_trusted_notebook_notification_widget();||')

# --------
# the ipythontutor magic
RUN pip install ipythontutor

# --------
# install jupyter extensions and enable the one about split cells
# to find out an extension's name
# look in the console in a jupyter that has it enabled
RUN pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install --system && jupyter nbextension enable splitcell/splitcell

# --------
# get the latest pandas (we need 0.21) and numpy while we are at it
RUN conda update -y numpy pandas

# --------
# install plotly for w7
RUN pip install plotly

