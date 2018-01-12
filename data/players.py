#!/usr/bin/env python3

import asyncio

import sys
import math
import random
import traceback
import argparse

# les 4 directions
actions = ('N', 'E', 'S', 'W')


class User:
    def __init__(self, name, period, cycles=None):
        self.name = name
        self.period = period
        # durer indéfiniment 
        self.cycles = cycles if cycles is not None else math.inf

    async def run(self):
        counter = 0
        while counter <= self.cycles:
            counter += 1
            duration = self.period * random.random()
            action = random.choice(actions)
            print(f"{action} {self.name}")
            await asyncio.sleep(duration)


class Players:
    def __init__(self, *users):
        self.users = list(users)

    async def run(self):
        jobs = [
            user.run() for user in self.users
            ]
        return await asyncio.gather(*jobs)


##########
players1 = Players(
    User('john', .8, 6),
    User('mary', .4, 12)
)


players2 = Players(
    User('bill', .5, 10),
    User('jane', .7, 7)
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(default=1, type=int, dest='group', nargs='?',
                        choices=(1,2),
                        help="select predefined group 1 or 2")
    args = parser.parse_args()
    players = players1 if args.group == 1 else players2

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(players.run())
        sys.exit(0)
    except Exception as e:
        print(f"EMERGENCY {type(e)}, {e}")
        sys.stderr.write(traceback.format_exc())
        sys.exit(1)
        

if __name__ == '__main__':
    main()
