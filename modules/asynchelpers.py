from datetime import datetime

import asyncio

# low-level API 
def _start_time():
    return datetime.now()

def _show_time(start, *args):
    delta = datetime.now() - start
    duration = f"{delta.seconds}s + {delta.microseconds//1000:03d}ms"
    print(duration, *args)

####################
# Use a module global to keep things simple

start = None

def start_time():
    global start
    print("---------- zero")
    start = _start_time()

def show_time(*args):
    _show_time(start, *args)

##############################
async def sequence(*messages, delay=1):
    show_time(">>>", *messages)
    await asyncio.sleep(delay)
    show_time("<<<", *messages)
    
