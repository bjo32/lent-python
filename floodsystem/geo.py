# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


from floodsystem.stationdata import build_station_list


build_station_list(use_cache=True)
from haversine import haversine, Unit
"""this function takes an imput of the list of stations and a tuple for coordinates p,
then makes a list of tuples containing the station and the distance to p in km. 
finnaly the list is sorted by distance in ascending order."""
def stations_by_distance(stations, p):
    sorted_tuples = []
    for station in stations:
        sorted_tuples.append((station.name, haversine(station.coord, p)))
    
    sorted_tuples = sorted_by_key(sorted_tuples, 1)
    return sorted_tuples

"""this function takes the list of stations, a tuple of coordinates for centre, float for radius r
values is an intermediate list of tuples created using the function 'stations_by_distance' of ordered stations by distance from centre
the items in the list with a redius less than r are added to a list called 'output', since values was ordered
the output is also ordered."""
def stations_within_radius(stations, centre, r):
    values = stations_by_distance(stations, centre)
    output = []


    for station in values:
        if station[1] < r:
            output.append(station)
        else:
            pass

    return output
