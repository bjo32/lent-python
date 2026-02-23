
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
