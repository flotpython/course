# @BEG@ 5 6 shipdict 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class Position(object):
    "a position atom with timestamp attached"
    
    def __init__(self, latitude, longitude, timestamp):
        "constructor"
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

# all these methods are only used when merger.py runs in verbose mode
    @staticmethod
    def _lat_str(f):
        if f>=0:        return "{}°N".format(f)
        else:           return "{}°S".format(-f)
    
    @staticmethod
    def _lon_str(f):
        if f>=0:        return "{}°E".format(f)
        else:           return "{}°W".format(-f)
        
    def lat_str(self):  return self._lat_str(self.latitude)
    def lon_str(self):  return self._lon_str(self.longitude)

    def __repr__(self):
        return "<{} {} @ {}".format(self.lat_str(),
                                    self.lon_str(), self.timestamp)
# @END@

# @BEG@ 5 6 shipdict-suite
class Ship(object):
    """
    a ship object, that requires a ship id, 
    and optionnally a ship name and country
    which can also be set later on
    
    this object also manages a list of known positions
    """
    def __init__(self, id, name=None, country=None):
        "constructor"
        self.id = id
        self.name = name
        self.country = country
        # this is where we remember the various positions over time
        self.positions = []

    def add_position(self, position):
        """
        insert a position relating to this ship
        positions are not kept in order so you need 
        to call `sort_positions` once you're done
        """
        self.positions.append(position)

    def sort_positions(self):
        """
        sort list of positions by chronological order
        """
        self.positions.sort(key=lambda position: position.timestamp)
# @END@

# @BEG@ 5 6 shipdict-suite
class ShipDict(dict):
    """
    a repository for storing all ships that we know about
    indexed by their id
    """
    def __init__(self):
        "constructor"
        dict.__init__(self)

    def __repr__(self):
        return "<ShipDict instance with {} ships>".format(len(self))

    @staticmethod
    def is_abbreviated(chunk):
        """
        depending on the size of the incoming data chunk, 
        guess if it is an abbreviated or extended data
        """
        return len(chunk) <= 7

    def add_abbreviated(self, chunk):
        """
        adds an abbreviated data chunk to the repository
        """
        id, latitude, longitude, _, _, _, timestamp = chunk
        if id not in self:
            self[id] = Ship(id)
        ship = self[id]
        ship.add_position (Position (latitude, longitude, timestamp))
        
    def add_extended(self, chunk):
        """
        adds an extended data chunk to the repository
        """
        id, latitude, longitude = chunk[:3]
        timestamp, name = chunk[5:7]
        country = chunk[10]
        if id not in self:
            self[id] = Ship(id)
        ship = self[id]
        if not ship.name:
            ship.name = name
            ship.country = country
        self[id].add_position (Position (latitude, longitude, timestamp))
# @END@

# @BEG@ 5 6 shipdict-suite
    def add_chunk(self, chunk):
        """
        chunk is a plain list coming from the JSON data and be either
        extended or abbreviated

        based on the result of is_abbreviated(), that chunk gets dealt with
        using add_extended or add_abbreviated
        """
        if self.is_abbreviated(chunk):
            self.add_abbreviated(chunk)
        else:
            self.add_extended(chunk)

    def sort(self):
        """
        makes sure all the ships have their positions in chronological order
        """
        for id, ship in self.iteritems():
            ship.sort_positions()

    def clean_unnamed(self):
        """
        Because we enter abbreviated and extended data
        in no particular order, and for any time period,
        we might have ship instances with no name attached
        This method removes such entries from the dict
        """
        # we cannot do all in a single loop as this would amount to
        # changing the loop subject
        # so let us collect the ids to remove first
        unnamed_ids = { id for id, ship in self.iteritems()
                        if ship.name is None }
        # and remove them next
        for id in unnamed_ids:
            del self[id]
# @END@

# @BEG@ 5 6 shipdict-suite
    def ships_by_name(self, name):
        """
        returns a list of all known ships with name <name>
        """
        return [ ship for ship in self.values() if ship.name == name ]

    def all_ships(self):
        """
        returns a list of all ships known to us 
        """
        return self.values()
# @END@
