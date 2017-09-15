#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pas utilisé dans un notebook pour les vidéos
# car c'est trop détiallé mais pourra servir
# pour un complément

import asyncio

from asynchelpers import start_timer, show_timer

async def countdown(ticks, quotient, period=1):
    """
    affiche un compte à rebours de ticks periodes
    puis retourne 1/quotient
    """
    n = ticks
    while n > 0:
        show_timer(f"tick{n}({quotient})")
        n -= 1
        await asyncio.sleep(period)
    show_timer(f"countdown ({ticks} x {period}) done")
    return 1 / quotient

tasks = [
    # va terminer normalement
    asyncio.ensure_future(countdown(2, quotient=1)),
    # lève une exception
    asyncio.ensure_future(countdown(3, quotient=0)),
]

start_timer()
asyncio.get_event_loop().run_until_complete(
    monitor_tasks(tasks, .8)
)

show_timer("cleaning up")
for i, task in enumerate(tasks):
    if not task.done():
        # monitor_task should exit only when all tasks are done
        show_timer("OOPS, this is unexpected")
    elif task.exception():
        show_timer(f"task: {i} has raised exception {task.exception()}")
    else:
        show_timer(f"task: {i} has returned {task.result()}")
