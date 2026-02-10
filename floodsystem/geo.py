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
def stations_by_distance(stations, p):
    sorted_tuples = []
    for station in stations:
        sorted_tuples.append((station.name, haversine(station.coord, p)))
    
    sorted_tuples = sorted_by_key(sorted_tuples, 1)
    return sorted_tuples

def stations_within_radius(stations, centre, r):
    values = stations_by_distance(stations, centre)
    output = []


    for station in values:
        if station[1] < r:
            output.append(station)
        else:
            pass

    return output
