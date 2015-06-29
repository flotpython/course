# -*- coding: utf-8 -*-

# for logging
import os
import os.path
import time

########## logging
def log_correction(exo_name, success):
    try:
        uid = os.getuid()
        md5 = os.path.basename(os.path.normpath(os.getenv("HOME")))
        now = time.strftime("%D-%H:%M", time.localtime())
        logname = os.path.join(os.getenv("HOME"), ".correction")
        message = "OK" if success else "KO"
        with open(logname, 'a') as log:
            line = "{now} {uid} {md5} {exo_name} {message}\n".format(**locals())
            log.write(line)
    except:
        pass

