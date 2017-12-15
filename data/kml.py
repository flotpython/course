#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# we use random to create different colors for ships
import random

# also we use the templating engine from string.Template
# see https://docs.python.org/2/library/string.html#template-strings
from string import Template


class KML():
    """
    An object to compute KML output for a set of ships

    # https://developers.google.com/kml/documentation/kml_tut#paths
    """

    random_inited = False

    def __init__(self):
        """
        First call to constructor will initialize the random seed so that
        successive runs produce the same set of colors
        """
        if not self.random_inited:
            random.seed(0)
            self.random_inited = True

    def _normalize(self, name):
        """
        We use ship names in XML ids - e.g. for linking the ship's 
        trajectory and its related style/color object
        But the XML syntax does not accept '&' 
        that we found in some ship names
        """
        # xxx a more robust version would need to be more thorough
        return name.replace("&", "")

    def _random_color(self):
        """
        https://developers.google.com/kml/documentation/kmlreference#color
        a KML color is aabbggrr 
        essentially the exact opposite of what you would expect
        we set alpha = 80 (128) and compute the other 3 in the 10-245 range
        """
        colors = [128] + [random.randint(10, 245) for i in range(3)]
        # format in hexadecimal on 2 caracters padded with zeroes if needed
        return "".join(["{:02x}".format(c) for c in colors])

    ####################
    def _ship_style(self, ship):
        """
        The KML fragment that describes a style for a given ship
        This is where we define the color to be used for each ship
        """

        template = Template("""<Style id="style_$ship_normal_name">
      <LineStyle>
        <color>$color</color>
        <width>4</width>
      </LineStyle>
      <PolyStyle>
        <color>ff000088</color>
      </PolyStyle>
    </Style>""")
        return template.substitute(ship_normal_name=self._normalize(ship.name),
                                   color=self._random_color())

    ####################
    def _ship_trip(self, ship):
        """
        The KML fragment that describes a trajectory as a <Placemark> tag
        The different coordinates are from the ship's positions, which
        of course need to have been sorted in chronological order first.
        """
        # the coordinates chunk
        coordinates = "\n".join([f"{position.longitude},{position.latitude},0"
                                 for position in ship.positions])

        # that we put into a <Placemark>
        # notice that the Placemark refers to the style created for that ship
        template = Template("""
    <Placemark>
      <name>$ship_normal_name</name>
      <description>Known positions for ship $ship_normal_name</description>
      <styleUrl>#style_$ship_normal_name</styleUrl>
      <LineString>
        <extrude>1</extrude>
        <tessellate>1</tessellate>
        <altitudeMode>relativeToGround</altitudeMode>
        <coordinates> $coordinates
        </coordinates>
      </LineString>
    </Placemark>
""")
        return template.substitute(ship_normal_name=self._normalize(ship.name),
                                   coordinates=coordinates)

    ####################
    def contents(self, ships, kml_name, description=None):
        """
        A complete KML document as a string, ready to be saved in a file

        kml_name and description are tags attached to the toplevel document
        and that will show up in google earth's navigation tool for example

        Each ship gets a dedicated color assigned randomly
        """

        description = description or "no description"

        # compute the list of all styles, just concatenated
        styles = "".join([self._ship_style(ship) for ship in ships])

        # compute the list of all ships trips, just concatenated
        placemarks = "".join([self._ship_trip(ship) for ship in ships])

        # https://developers.google.com/kml/documentation/kml_tut#paths
        template = Template(  # must start on line 1
            """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>$kml_name</name>
    <description>$description</description>
  $styles
  $placemarks
  </Document>
</kml>
""")
        return template.substitute(kml_name=kml_name, description=description,
                                   placemarks=placemarks, styles=styles)
