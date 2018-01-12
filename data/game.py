#!/usr/bin/env python3

import asyncio

import sys

from subprocess import PIPE


class Game:


    def __init__(self):
        self.running = 0
        self.counter = 1
        self.clock_seconds = 0
        pass


    def read_stdin_line(self, stdin):
        line = stdin.readline().strip()
        print(f">> {line}")
        if not line:
            return
        elif line.lower().startswith('q'):
            print('bye')
            sys.exit(0)
        asyncio.ensure_future(self.fork_players(line))


    async def read_and_display(self, stream, worker, streamname):
        while True:
            bytes = await stream.readline()
            if not bytes:
                break
            line = bytes.decode().strip()
            print(f"received line `{line}` on {streamname} from {worker}")
    
        
    async def fork_players(self, groupnb):
        try:
            nb = int(groupnb)
            if not (1 <= nb <= 4):
                raise ValueError('entre 1 et 4')
        except Exception as e:
            print(f"{groupnb} doit être entre 1 et 4 {type(e)} - {e}")
            return
        # python -u pour que le processus fils ne bufferise pas ses sorties
        # on pourrait aussi le faire dans players.py avec ceci
        # sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
        command = f"python3 -u data/players.py {groupnb}".split()
        
        worker = f"group {nb} - process #{self.counter}"
        self.counter += 1
        self.running += 1
        process = await asyncio.create_subprocess_exec(
            *command, 
            stdout = PIPE, stderr = PIPE, 
        )
        stdout, stderr = await asyncio.gather(
            self.read_and_display(process.stdout, worker, 'stdout'),
            self.read_and_display(process.stderr, worker, 'stderr'))
        retcod = await process.wait()
        print(f"worker {worker} is over with -> {retcod}")
        self.running -= 1
        return retcod

    async def clock(self):
        while True:
            print(f"clock = {self.clock_seconds:04d}s - {self.running} running procs")
            await asyncio.sleep(1)
            self.clock_seconds += 1

    def mainloop(self):
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(self.clock())
        loop.add_reader(
            # le filedescriptor qui nous intéresse
            sys.stdin.fileno(),
            # la callback
            Game.read_stdin_line,
            # les arguments de la callback
            self, sys.stdin)
        loop.run_forever()


##########
def main():
    Game().mainloop()


if __name__ == '__main__':
    main()
