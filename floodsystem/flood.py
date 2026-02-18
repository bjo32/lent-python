"""Functions for analysing station water levels for flood warnings.

This is the ``flood`` submodule mentioned in the coursework spec.
"""

from typing import List, Tuple

from floodsystem.station import MonitoringStation


def stations_over_threshold(stations: List[MonitoringStation], tol: float) -> List[Tuple[MonitoringStation, float]]:
    """Return a list of ``(station, relative_level)`` tuples.

    Each tuple holds a station whose *latest relative water level* is
    strictly greater than ``tol`` and the corresponding relative level.
    The returned list is sorted in **descending** order of relative level.

    ``relative level`` is the value returned by
    :meth:`MonitoringStation.relative_water_level`.

    Parameters
    ----------
    stations:
        Iterable of :class:`~floodsystem.station.MonitoringStation`
    tol:
        Threshold value (e.g. ``0.8`` means 80% of typical range).

    Returns
    -------
    list of tuples
        Station/level pairs sorted high-to-low by level. Stations for which
        the level is ``None`` or the typical range is inconsistent are
        ignored.
    """

    over: List[Tuple[MonitoringStation, float]] = []
    for s in stations:
        level = s.relative_water_level()
        if level is None:
            continue
        if level > tol:
            over.append((s, level))

    # sort by the second element (level) in reverse order
    return sorted(over, key=lambda pair: pair[1], reverse=True)
