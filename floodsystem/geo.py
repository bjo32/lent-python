# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sort_by_key  # noqa


from floodsystem.stationdata import build_station_list


build_station_list(use_cache=True)
from haversine import haversine, Unit
def stations_by_distance(stations, p):
    sorted_tuples = []
    for station in stations:
        sorted_tuples.append((station.name, haversine(station.coord, p)))
    
    sorted_tuples = sort_by_key(sorted_tuples, 1)
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


# 1D
def rivers_with_station(stations):
    """
    Returns a set of the names of the rivers with a monitoring station.
    """
    rivers = set()
    for station in stations:
        if station.river:       # ensure station has river 
            rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    """
    Returns a dictionary that maps river names to a list of station objects
    on a given river.
    """
    rivers_dict = {}
    for station in stations:
        river_name = station.river
        if river_name not in rivers_dict:
            rivers_dict[river_name] = []
        rivers_dict[river_name].append(station)
        
    return rivers_dict

# 1E

def rivers_by_station_number(stations, N):
    """
    Returns a list of (river name, number of stations) tuples, 
    sorted by the number of stations. 
    In the case that there are more rivers with the same number of stations 
    as the Nth entry, these rivers are included in the list.
    """
    
    stations_on_rivers = stations_by_river(stations)
    

    count_list = []
    for river, station_list in stations_on_rivers.items():
        count_list.append((river, len(station_list)))
    

    count_list.sort(key=lambda x: (-x[1], x[0]))
    

    if N >= len(count_list):
        return count_list
    

    threshold_count = count_list[N-1][1]
    

    result = count_list[:N]
    

    for i in range(N, len(count_list)):
        if count_list[i][1] == threshold_count:
            result.append(count_list[i])
        else:
            break
            
    return result


