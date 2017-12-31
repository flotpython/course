#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version : 3.0

# standard library imports
import gzip
import json
import glob
from argparse import ArgumentParser
#

# application imports
from shipdict import ShipDict
from kml import KML
from compare import Compare

########################################


class Merger(object):

    def __init__(self):
        """
        constructor creates an ArgumentParser object to implement main interface
        puts resulting args in self.args
        also creates an empty instance of ShipDict for merging incoming data
        """
        parser = ArgumentParser()
        parser.add_argument("-v", "--verbose", dest='verbose', default=False,
                            action='store_true',
                            help="Verbose mode")
        parser.add_argument("-s", "--ship", dest='ship_name', default=None,
                            action='store',
                            help="Restrict to ships by that name")
        parser.add_argument("-z", "--gzip", dest='gzip', default=False,
                            action='store_true',
                            help="Store kml output in gzip (KMZ) format")
        parser.add_argument("inputs", nargs='*')
        self.args = parser.parse_args()

        # the windows command line is a little lazy with filename expansion
        inputs = []
        for input in self.args.inputs:
            if '*' not in input:
                inputs.append(input)
            else:
                inputs.extend(glob.glob(input))
        self.args.inputs = inputs

        self.ship_dict = ShipDict()

    def merge(self, json_input_filenames):
        """
        given a list of json filenames, decode the JSON content
        and insert it into the local instance of ShipDict
        """
        for json_input_filename in json_input_filenames:

            # self.args.verbose is True if we run the program with --verbose
            if self.args.verbose:
                print(f"Opening {json_input_filename} for parsing JSON")

            with open(json_input_filename, newline="\n") as feed:
                # decode json
                chunks = json.load(feed)
                # each incoming file contains a list of
                # extended or abbreviated chunks
                for chunk in chunks:
                    self.ship_dict.add_chunk(chunk)

        # at this point it might be that some of the ships
        # in ship_dict were never seen in an extended dataset
        # in that case we do not have a name for these ships
        # so we silently ignore them
        self.ship_dict.clean_unnamed()

        # we also might need to sort positions
        # since we cannot be sure of the order
        # in which data files are provided
        self.ship_dict.sort()

    def write_ships_summary(self, ships, out_name):
        """
        saves in filename a summary of all selected ships
        typically out_name is <ship_name>.txt or ALL_SHIPS.txt 
        also it will have a -v added in verbose mode
        as we show more stuff in verbose mode

        ships are expected to be sorted already

        returns filename
        """
        filename = f"{out_name}-v.txt" if self.args.verbose else f"{out_name}.txt"

        print(f"Opening {filename} for listing ships")

        with open(filename, 'w', newline="\n") as summary:
            # one line to say how many ships we have seen
            summary.write(f"Found {len(ships)} ships\n")
            # ships are expected to be sorted already
            for ship in ships:
                summary.write(
                    f"{ship.name} ({len(ship.positions)} positions)\n")
                # in verbose mode let us show all the positions at hand
                if self.args.verbose:
                    for position in ship.positions:
                        summary.write(f"{position}\n")
        # return filename
        return filename

    def write_kml_output(self, ships, out_name):
        """
        saves a summary of all selected ships in KML format
        (or KMZ if gzip option selected)
        out_name is used to compute the output filename
        returns filename
        """
        # create an instance of the KML class
        kml = KML()
        # send it the `contents` method to retrieve the text
        # to be written in the kml file
        contents = kml.contents(ships, kml_name=out_name,
                                description=f"Positions for ship(s) {out_name}"
                                )
        # compute suffix based on self.args.gzip
        #  - whether the --gzip option was passed or not
        suffix = "kmz" if self.args.gzip else "kml"
        # compute full filename
        kml_filename = f"{out_name}.{suffix}"
        # message
        print(f"Opening {kml_filename} for ship {out_name}")
        # open a plain file or compressed file as requested
        with gzip.open(kml_filename, 'w', newline="\n") if self.args.gzip \
                else open(kml_filename, 'w', newline="\n") as out:
            out.write(contents)
        # return filename
        return kml_filename

    def main(self):
        """
        program entry point

        first runs merge on the input json filenames
        specified on the command line

        then creates a summary file, and a kml file

        as per usual convention, this returns 0 if everything goes fine
        and non-zero otherwise, and specifically
          (*) 1 if both output files were created but they do not match 
              the reference result
          (*) 2 if an exception occured and prevented file creation

        run with --help to see the list of available options
        in particular it is possible to restrict to the ship(s) that match
        one specific ship name using -s/--ship
        """
        try:
            # send the contents of all incoming files to the ship_dict instance
            # this method also clears
            self.merge(self.args.inputs)

            # if --ship is specified on the command line,
            # corresponding value is stored in self.args.ship_name
            # as per ArgumentParser definition. So:

            # if --ship is not specified
            if not self.args.ship_name:
                # use all ships in ship_dict
                ships = self.ship_dict.all_ships()
                # we use this to compute output filenames
                output_name = "ALL_SHIPS"

            # if --ship was specified
            else:
                # restrict to ships that match the selected ship name
                ships = self.ship_dict.ships_by_name(self.args.ship_name)
                output_name = self.args.ship_name

            # sort ships once and for good
            # we can't sort these objects inline as they are
            # typically dict_values objects
            ships = sorted(ships, key=lambda ship: ship.name)

            # create summary file
            summary_filename = self.write_ships_summary(ships, output_name)

            kml_filename = self.write_kml_output(ships, output_name)

            # if a ship name was specified, we cannot compare anything
            if self.args.ship_name:
                ok = True
            else:
                # for each of the 2 files, compare contents with the reference
                # that is expected to be in this directory with a .ref extension
                ok_summary = Compare(summary_filename).compare_and_print()
                ok_kml = Compare(kml_filename).compare_and_print()
                # is everything fine ?
                ok = ok_summary and ok_kml
            # if so return 0 otherwise 1
            return 0 if ok else 1

        # if anything goes south
        except Exception as e:
            # give description of the exception
            print('Something went wrong', e)
            # plus provide a snapshot of the stack at the point
            # where the exception was raised
            import traceback
            traceback.print_exc()
            # return 2 in this case
            return 2


# if this not loaded as part of an `import` statement
if __name__ == '__main__':
    # create a Merger instance
    merger = Merger()
    # send it the main method and transmit this return code right to wait()
    exit(merger.main())
