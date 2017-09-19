from datetime import datetime

import asyncio

# low-level API 
def _start_timer():
    return datetime.now()

def _show_timer(start, *args):
    delta = datetime.now() - start
    duration = f"{delta.seconds}s + {delta.microseconds//1000:03d}ms"
    print(duration, *args)

####################
# Use a module global to keep things simple

glo_start = None

def start_timer():
    global glo_start
    print("---------- zero")
    glo_start = _start_timer()

def show_timer(*args):
    global glo_start
    _show_timer(glo_start, *args)

##############################
async def sequence(*messages, delay=1):
    show_timer(">>>", *messages)
    await asyncio.sleep(delay)
    show_timer("<<<", *messages)
    
##########
def reset_loop():
    asyncio.set_event_loop(asyncio.new_event_loop())


