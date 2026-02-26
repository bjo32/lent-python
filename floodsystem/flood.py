
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

def flood_risk(stations):
    """Return a list of stations at risk of flooding, sorted in descending order by relative water level."""
    warnings = []
    for s in stations:
        if not s.typical_range_consistent():
            continue
        rel = s.relative_water_level()
        if rel is None:
            continue
        if rel > 1.0:  # severe flood risk
            warnings.append((s.town, rel, "severe"))
        elif rel > 0.8:  # high flood risk
            warnings.append((s.town, rel, "high"))
        elif rel > 0.6:  # moderate flood risk
            warnings.append((s.town , rel, "moderate"))
        else:  # low flood risk
            warnings.append((s.town, rel, "low"))
    return warnings
