
# floodsystem/flood.py
# functions relating to flood analysis

from floodsystem.utils import sort_by_key


def stations_level_over_threshold(stations, tol):
    """Return list of (station, relative level) tuples for stations
    whose relative water level is strictly greater than *tol*.

    The returned list is sorted in descending order by relative level.
    Stations with inconsistent typical ranges or missing levels are
    ignored.
    """

    over = []
    for s in stations:
        # skip stations with bad typical range data
        if not s.typical_range_consistent():
            continue
        rel = s.relative_water_level()
        if rel is None:  # no recent reading
            continue
        if rel > tol:
            over.append((s, rel))

    # sort by the second element (relative level) in descending order
    return sort_by_key(over, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    """Return list of the N stations with the highest relative water
    levels, in descending order of relative level. Stations with
    inconsistent typical ranges or missing levels are ignored.
    """

    over = []
    for s in stations:
        # skip stations with bad typical range data
        if not s.typical_range_consistent():
            continue
        rel = s.relative_water_level()
        if rel is None:  # no recent reading
            continue
        over.append((s, rel))

    # sort by the second element (relative level) in descending order
    over = sort_by_key(over, 1, reverse=True)

    return over[:N]



def town_flood_warnings(stations):
    town_max_level = {}
    
    for station in stations:

        if station.town is None:
            continue
            
        rel_level = station.relative_water_level()
        if rel_level is None:
            continue
            

        if station.town not in town_max_level or rel_level > town_max_level[station.town]:
            town_max_level[station.town] = rel_level
            
    warnings = []
    
    for town, level in town_max_level.items():
        if level >= 2.0:
            risk = 'Severe'
        elif level >= 1.5:
            risk = 'High'
        elif level >= 1.0:
            risk = 'Moderate'
        else:
            risk = 'Low'
            
        warnings.append((town, risk))
        
    return warnings
