
from ast import List, Tuple
from floodsystem.station import MonitoringStation
from floodsystem.utils import sort_by_key


def stations_level_over_threshold(stations, tol):

    over = []
    for station in stations:
        level = station.relative_water_level()
        if level is None:
            continue
        if level > tol:
            over.append((station, level))

    # sort by the second element (level) in reverse order
    return sort_by_key(over, key=lambda pair: pair[1], reverse=True)
