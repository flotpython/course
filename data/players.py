#!/usr/bin/env python3

import asyncio

import sys
import math
import random
import traceback
import argparse


class Player:

    # les 4 directions
    directions = ('N', 'E', 'S', 'W')

    def __init__(self, name, period, cycles):
        self.name = name
        self.period = period
        # durer indéfiniment
        self.cycles = cycles

    async def run(self):
        counter = 0
        while counter <= self.cycles:
            counter += 1
            duration = self.period * random.random()
            direction = random.choice(self.directions)
            print(f"{direction} {self.name}")
            await asyncio.sleep(duration)


class Players:
    def __init__(self, *players):
        self.players = list(players)

    async def run(self):
        jobs = [
            player.run() for player in self.players
        ]
        return await asyncio.gather(*jobs)


##########
predefined = {
    # circa 3s
    1: Players(Player('john', .8, 3),
               Player('mary', .4, 7),
               ),
    2: Players(Player('bill', .5, 5),
               Player('jane', .7, 4),
               ),
    # circa 6s
    3: Players(Player('augustin', .8, 8),
               Player('randalph', .6, 10),
               ),
    4: Players(Player('bertrand', .5, 12),
               Player('juliette', .7, 8),
               ),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(default=1, type=int, dest='groupnb', nargs='?',
                        choices=(1, 2, 3, 4),
                        help="select predefined group 1 or 2")
    args = parser.parse_args()
    players = predefined[args.groupnb]

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
