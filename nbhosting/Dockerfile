# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM jupyter/scipy-notebook:latest


# --------
# for interfacing with nbhosting, we need this startup script in all images
# and we need to be root again for installing stuff
USER root
COPY start-in-dir-as-uid.sh /usr/local/bin


# --------
# this is to increase the ulimit -n (max nb of open files)
# as perceived by regular user processes in the container
# before we implement this setting, default was 1024
# 128 * 1024 looks about right
# container root was OK at 1024*1024
RUN for type in hard soft; do echo '*' $type nofile 131072 ; done > /etc/security/limits.d/open-file.conf


# --------
# add lsof in the mix to help troubleshoot shortages of open files
RUN apt-get update && apt-get install lsof


# --------
# hacks for jupyter itself
# (*) disable check done when saving files - see https://github.com/jupyter/notebook/issues/484
# (*) disable the 'Trusted' notification widget
# (#) remove the 'Notebook saved' message that annoyingly pops up
RUN (find /opt /usr -name notebook.js -o -name main.min.js | xargs sed -i -e 's|if (check_last_modified)|if (false)|') \
 &&  (find /opt /usr -name notificationarea.js -o -name main.min.js | \
      xargs sed -i \
      -e 's|this.init_trusted_notebook_notification_widget();||' \
      -e 's|nnw.set_message(i18n.msg._("Notebook saved"),2000);||' \
      )


# --------
# use latest pip
RUN pip install -U pip


# --------
# auto-evaluated exercices
RUN pip install nbautoeval


# --------
# the ipythontutor magic
RUN pip install ipythontutor


# --------
# go back to tornado-4.5.3 for asyncio 
RUN pip install tornado==4.5.3


# --------
# install jupyter extensions and enable the one about split cells
# to find out an extension's name
# look in the console in a jupyter that has it enabled
RUN pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install --system && jupyter nbextension enable splitcell/splitcell


# --------
# install plotly for w7
RUN pip install plotly
