#!/usr/bin/env python

"""
A utility run one-shot to remove duplicate ships
i.e. those that have same name but differents ids
"""


from __future__ import print_function
from glob import glob
import json
import os

def pass1():

    # the set of all tuples (id, name)
    all_tids = set()

    sources = glob("*--ext.json")

    for source in sources:
        print("pass 1 - opening source {}".format(source))
        with open(source) as feed:
            extended = json.load(feed)
        for e in extended:
            all_tids.add( (e[0], e[6]) )

    # find ids to remove
    duplicate_ids = set()
    all_names = set()
    for id, name in all_tids:
        if name not in all_names:
            all_names.add(name)
        else:
            print("Found duplicate {} - {}".format(id, name))
            duplicate_ids.add(id)
    return all_tids, duplicate_ids

def pass2(all_tids, duplicate_ids):

    sources = glob("*.json")
    for source in sources:
        print("pass 2 - opening source {}".format(source))
        with open(source) as feed:
            ships = json.load(feed)
            preserved_ships = []
            for ship in ships:
                if ship[0] in duplicate_ids:
                    print("Ignoring entry {} in source {}"
                          .format(ship, source))
                else:
                     preserved_ships.append(ship)
            new_source = source + ".new"
            with open(new_source, 'w') as output:
                json.dump(preserved_ships, output)
            print("Saved {}".format(new_source))
        
def pass3():
    new_files = glob("*.new")
    for new_file in new_files:
        old_file = new_file.replace(".new", "")
        print("Renaming {} into {}".format(new_file, old_file))
        os.rename(new_file, old_file)


def main():
    all_tids, duplicate_ids = pass1()
    pass2(all_tids, duplicate_ids)
    pass3()

if __name__ == '__main__':
    main()
