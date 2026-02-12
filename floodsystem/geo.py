# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sort_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    """Takes a list of stations and a tuple for coordinates p.
    Returns a list of tuples containing the station name and the distance to p in km.
    The list is sorted by distance in ascending order.
    """
    sorted_tuples = []
    for station in stations:
        sorted_tuples.append((station.name, haversine(station.coord, p, unit=Unit.KILOMETERS)))
    
    sorted_tuples = sort_by_key(sorted_tuples, 1)
    return sorted_tuples


def stations_within_radius(stations, centre, r):
    """Returns stations within a given radius of a centre point.
    Takes list of stations, a tuple of coordinates for centre, and float for radius r.
    Returns a list ordered by distance from centre.
    """
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
    Use a set to automatically handle deduplication
    """
    rivers = set()
    for station in stations:
        if station.river:       # ensure station has a valid river name
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
    
    stations_on_rivers = stations_by_river(stations)
    
    """
    Returns a list of (river name, number of stations) tuples
    """
    count_list = []
    for river, station_list in stations_on_rivers.items():
        count_list.append((river, len(station_list))) #name, number of stations
    
    """
    sort the list by the number of stations. 
    """
    count_list.sort(key=lambda x: (-x[1], x[0]))        
    #x[1]is number of station in each element, (-) to ensure descending list
    #when number same, sort by name

    if N >= len(count_list):
        return count_list
    

    threshold_count = count_list[N-1][1]        #get the count of the Nth river
    

    result = count_list[:N]
    
    """
    if there are more rivers with the same number of stations as the Nth entry, these rivers are included in the list.
    """
    for i in range(N, len(count_list)):
        if count_list[i][1] == threshold_count:
            result.append(count_list[i])
        else:
            break
            
    return result


