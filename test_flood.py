"""Unit tests for the flood submodule."""

from floodsystem.flood import stations_over_threshold
from floodsystem.station import MonitoringStation


def make_station(level, trange=(0.0, 1.0)):
    """create a dummy station with given latest level and typical range."""
    s = MonitoringStation("id", "mid", "label", (0, 0), trange, "river", "town")
    s.latest_level = level
    return s


def test_stations_over_threshold_basic():
    # two stations: one exactly at threshold, one above
    s1 = make_station(0.5, (0.0, 1.0))  # relative level 0.5
    s2 = make_station(0.8, (0.0, 1.0))  # relative level 0.8
    result = stations_over_threshold([s1, s2], 0.5)
    assert len(result) == 1
    st, lvl = result[0]
    assert st is s2
    assert lvl == 0.8


def test_stations_over_threshold_sorting():
    s1 = make_station(0.2, (0.0, 1.0))  # rel 0.2
    s2 = make_station(0.7, (0.0, 1.0))  # rel 0.7
    s3 = make_station(0.9, (0.0, 1.0))  # rel 0.9
    result = stations_over_threshold([s1, s2, s3], 0.1)
    # all three exceed threshold; order should be descending by relative level
    assert [r[0] for r in result] == [s3, s2, s1]


def test_excludes_none_and_inconsistent():
    s_none = make_station(None)
    s_bad = make_station(0.5, (2.0, 1.0))  # inconsistent typical range
    s_good = make_station(0.5)
    result = stations_over_threshold([s_none, s_bad, s_good], 0.0)
    assert result == [(s_good, 0.5)]
