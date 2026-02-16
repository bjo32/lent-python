
from floodsystem import station, stationdata
from floodsystem.station import relative_water_level
from floodsystem.utils import sort_by_key
stations = stationdata.build_station_list()



def stations_level_over_threshold(stations, tol):
    """returns a list of tuples, where each tuple holds 
    (i) a station (object) at which the latest relative water level is over tol and 
    (ii) the relative water level at the station.
    The returned list should be sorted by the relative level in descending order. 
    The function should have the signature:"""
    over_threshold = []
    for station in stations:
        relative_level = station.relative_water_level(station)
        if relative_level is not None and relative_level > tol:
            over_threshold.append((station, relative_level))
    
    over_threshold = sort_by_key(over_threshold, 1, reverse=True)  # Sort by relative level in descending order
    return over_threshold
