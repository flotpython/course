#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# dealing with filenames
import os.path
# for formatting timestamps
import time
# using izip rather than zip
import itertools
# downloading data
import urllib.request
import urllib.error
import urllib.parse
# uncompress data
import gzip
# unmarshalling JSON data
import json
# for showing a sample
import copy
import pprint

from argparse import ArgumentParser

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

# datetime_format="%Y-%m-%d:%H-%M"
# def datetime_repr(timestamp):
#    return time.strftime(datetime_format,time.gmtime(timestamp))
date_format = "%Y-%m-%d"


def date_repr(timestamp):
    return time.strftime(date_format, time.gmtime(timestamp))

KELVIN = 273.15


def xpath(entry, path):
    """
    helper function to extract a piece from a complex data 
    using a succession of keys or indices
    e.g.
    if dict = {'city': {'coord': {'lat': 49.55, 'lon': 1.62}}}
    then
    xpath (dict, ('city', 'coord', 'lon')) returns 1.62
    and
    xpath (dict, 'city/coord/lon')) returns 1.62 as well
    """
    if isinstance(path, str):
        path = path.split('/')
    result = entry
    for key in path:
        result = result[key]
    return result


# like in css we do: top right bottom left
class RectangleArea(object):

    def __init__(self, *args):
        """
        constructor
        can take either 4 numbers top, right, bottom and left
        or a single string with these values comma-separated

        known limitation : cannot select a rectangle
        over the international date line
        """
        # 4 arguments - we need numbers then
        if len(args) == 4:
            self.corners = tuple(args)
        # 1 argument - a string then
        elif len(args) == 1:
            self.corners = [float(x) for x in args[0].split(',')]

    def __repr__(self):
        return "Top {} Right {} Bottom {} Left {}".format(*self.corners)

    def covers_lat_lon(self, lat_lon_rec):
        """
        tells if a point, represented as a dict with the
        'lat' and 'lon' keys as in the native JSON format,
        belongs in this area

        return a bool
        """
        (top, right, bottom, left) = self.corners
        lon = lat_lon_rec['lon']
        lat = lat_lon_rec['lat']
        return lon >= left and lon <= right and\
            lat >= bottom and lat <= top

    def covers_city(self, city):
        return self.covers_lat_lon(xpath(city, 'city/coord'))


def load_cities(filename):
    """
    This function loads a JSON file
    which may be gzipped

    returns a list of city-records
    or None if if was not possible to open that file
    """
    if not os.path.isfile(filename):
        return None
    # try to decode a plain file
    try:
        with open(filename) as input:
            return [json.loads(line) for line in input if line]
    except:
        pass
    # try to decode a gzipped file
    try:
        with gzip.open(filename) as input:
            return [json.loads(line) for line in input if line]
    except:
        pass
    return None

# used to produce the text for the notebook


def show_sample_city(city_record):
    """
    used to produce the notebook that describes the exercise

    pretty print a city record 
    with only the first data record mentioned
    """
    sample = copy.deepcopy(city_record)
    data = xpath(sample, 'data')
    data[1:] = ['... other similar dicts ...']
    pprint.pprint(sample)


def plot_1d(cities):
    """
    visualize temperature in the first city
    for all available dates
    """
    # find the first selected city
    city = None
    for c in cities:
        if 'selected' in c:
            city = c
    if not city:
        print('No city selected for plot_1d')
        return

    points_per_day = ('morn', 'day', 'eve', 'night')
    nb_per_day = len(points_per_day)

    T = [measure['temp'][key] - KELVIN
         for measure in city['data']
         for key in points_per_day]
    X = list(range(1, len(T) + 1))

    bar_plot = plt.bar(X, T, 0.1)

    plt.ylabel('℃')
    plt.title('Temperatures in {}'.format(xpath(city, 'city/name')))

    D = [date_repr(measure['dt']) for measure in city['data']]
    Dx = [4 * n + 2 for n in range(len(city['data']))]
    plt.xticks(Dx, D, rotation='vertical')
    # plt.yticks(np.arange(0,81,10))
    #plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

    plt.show()


def plot_2d(cities):
    """
    visualize the positions of all cities on a 2D map
    """
    LON_s = [xpath(city, 'city/coord/lon') for city in cities]
    LAT_s = [xpath(city, 'city/coord/lat') for city in cities]
    # emphasize selected cities with a specific size and color
    # 'r' stands for red, 'b' is black
    colors = ['r' if 'selected' in city else 'b' for city in cities]
    sizes = [100 if 'selected' in city else .1 for city in cities]
    plt.scatter(LON_s, LAT_s, c=colors, s=sizes)

    # to exit the drawing, close related window
    plt.show()


def plot_3d(cities):
    """visualize pressure in 3D
    position as (x, y) and pressure as z

    to keep it simple we take the pressure from the first measure
    available in each city - which may be a little inaccurate
    as not all 1st measure points are guaranteed 
    to be for the exact same date

    likewise the date that gets displayed is extracted 
    from the *first* city as a rough approximation
    """

    # base all measures on first day present in each city
    day = 0
    # date time for the label
    dt = xpath(cities[0], ('data', day, 'dt'))
    date = date_repr(dt)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = [xpath(city, ('city', 'coord', 'lon')) for city in cities]
    Y = [xpath(city, ('city', 'coord', 'lat')) for city in cities]
    P = [xpath(city, ('data', day, 'pressure'))
         for city in cities]
    ax.plot_trisurf(X, Y, P, cmap=cm.jet, linewidth=0.2,
                    label="Pressure on %s" % date)
    ax.set_title("Pressure on %s" % date)
    plt.show()


def main():
    parser = ArgumentParser()
    parser.add_argument("-c", "--crop", dest='crop', default=None,
                        help="""specify a region for cropping
                        regions are rectangular areas and can be specified 
                        as a comma-separated list of 4 numbers for
                        north, east, south, west""")
    parser.add_argument("-n", "--name", dest='select_names', default=[],
                        action='append',
                        help="cumulative - select cities by this name(s)")
    parser.add_argument("-a", "--all", dest='select_all', default=False,
                        action='store_true',
                        help="select all cities")
    parser.add_argument("-l", "--list", dest="list_cities", default=False,
                        action='store_true',
                        help="If set, selected city names get listed")
    parser.add_argument("-1", "--1d", dest="plot_1d", default=False,
                        action='store_true',
                        help="""Display a bar chart for the pressure
                        in the first selected city""")
    parser.add_argument("-2", "--2d", dest="plot_2d", default=False,
                        action='store_true',
                        help="""Display a 2D diagram of the 
                        positions of selected cities""")
    parser.add_argument("-3", "--3d", dest="plot_3d", default=False,
                        action='store_true',
                        help="""Display a 3D diagram of the 
                        pressure in all cities""")

    parser.add_argument("filename", help="input JSON file - might be gzipped")
    args = parser.parse_args()

    # always load input file
    cities = load_cities(args.filename)
    if not cities:
        print("Cannot open input {}".format(args.filename))
        return 1
    print(10 * '-', "From {}\n\tdealing with {} cities".
          format(args.filename, len(cities)))

    # crop if specified
    if args.crop:
        crop_area = RectangleArea(args.crop)
        cities = [city for city in cities if crop_area.covers_city(city)]
        print(10 * '-', "After cropping with {}\n\tdealing with {} cities".
              format(crop_area, len(cities)))

    # mark the ones selected by their name if specified with --name
    if args.select_all:
        for city in cities:
            city['selected'] = True
    elif args.select_names:
        # lowercase all
        args.names = [name.lower() for name in args.select_names]
        selected = 0
        for city in cities:
            if xpath(city, 'city/name').lower() in args.select_names:
                city['selected'] = True
                selected += 1
    selected = [xpath(city, 'city/name')
                for city in cities if 'selected' in city]
    if selected:
        print(10 * '-', "Selected {} cities\n\t{}".
              format(len(selected), selected))
    else:
        print(10 * '-', "No city selected")

    # display selected cities by name and # of measures with --list
    if args.list_cities:
        cities.sort(key=lambda city: xpath(city, 'city/name'))
        for city in cities:
            message = " SELECTED" if 'selected' in city else ""
            print("{} ({} measures) {}".format(xpath(city, 'city/name'),
                                               len(xpath(city, 'data')),
                                               message))

    # show plots as requested
    if args.plot_1d:
        plot_1d(cities)

    if args.plot_2d:
        plot_2d(cities)

    if args.plot_3d:
        plot_3d(cities)


if __name__ == '__main__':
    main()
