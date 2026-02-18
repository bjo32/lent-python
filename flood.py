from floodsystem import station, stationdata
from floodsystem.utils import sort_by_key

stations = stationdata.build_station_list()


def stations_level_over_threshold(stations, tol):
    """Return (station, relative level) tuples for stations exceeding tol.
    """
    over_threshold = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None and relative_level > tol:
            over_threshold.append((station, relative_level))
    
    # sort by the second element (level) descending
    return sort_by_key(over_threshold, 1, reverse=True)

print(stations_level_over_threshold(stations, 0.8))