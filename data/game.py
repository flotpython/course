#!/usr/bin/env python3

import asyncio

import sys

from subprocess import PIPE


class Scheduler:

    def __init__(self, script):
        """
        Un script est un itérable de tuples de la forme
        time_predef = (secondes, predef)
        predef étant un nombre de 1 à 4 qui fait références aux configurations
        prédéfinies de players.py
        """

        # on trie le script par ordre chonologique
        self.script = list(script)
        self.script.sort(key = lambda time_predef : time_predef[0])

        # pour savoir où on en est
        self.counter = 1
        # combien de process sont actifs
        self.running = 0

    async def run(self):
        epoch = 0
        for tick, predef in self.script:
            # attendre le bon moment
            await asyncio.sleep(tick - epoch)
            # pour le prochain
            epock = tick
            asyncio.ensure_future(self.fork_players(predef))

    async def fork_players(self, predef):
        # la commande à lancer pour forker une instance de players.py
        command = f"python3 -u data/players.py {predef}".split()
        # un nom un peu plus parlant
        worker = f"process #{self.counter} (predef {predef})"
        self.counter += 1
        self.running += 1
        # c'est là que ça se passe : on forke
        print(8 * '>', f"worker {worker}")
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=PIPE, stderr=PIPE,
        )
        # et on attend
        stdout, stderr = await asyncio.gather(
            self.read_and_display(process.stdout, worker, 'stdout'),
            self.read_and_display(process.stderr, worker, 'stderr'))
        retcod = await process.wait()
        # un process se termine
        print(8 * '<', f"worker {worker} - exit code {retcod}")
        self.running -= 1
        # si c'était le dernier on sort de là
        if self.running == 0:
            asyncio.get_event_loop().stop()
        return retcod
                    
    async def read_and_display(self, stream, worker, streamname):
        while True:
            bytes = await stream.readline()
            if not bytes:
                break
            line = bytes.decode().strip()
            print(8 * ' ', f"got `{line}` on {streamname} from {worker}")


class Clock:

    def __init__(self):
        self.clock_seconds = 0

    async def run(self):
        while True:
            #print(f"clock = {self.clock_seconds:04d}s - {self.running} running procs")
            print(f"clock = {self.clock_seconds:04d}s")
            await asyncio.sleep(1)
            self.clock_seconds += 1

    
class Game:

    def __init__(self, script):
        self.script = script

    def mainloop(self):
        loop = asyncio.get_event_loop()

        clock = Clock()
        asyncio.ensure_future(clock.run())

        scheduler = Scheduler(self.script)
        asyncio.ensure_future(scheduler.run())
        loop.run_forever()


##########
if __name__ == '__main__':

    # predefined scenario is to fork 10 players
    
    predef_script = [
#        (0, 3), (.5, 4), (1., 1), (1.5, 2),
        (0, 1), (0.5, 2),
        ]
    
    Game(predef_script).mainloop()
