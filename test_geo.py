from floodsystem.geo import haversine, stations_by_distance, rivers_with_station, stations_by_river, rivers_by_station_number, stations_within_radius 
from floodsystem.stationdata import build_station_list
def test_stations_by_distance():
     stations = build_station_list()
p = (52.2053, 0.1218)
distance_list = stations_by_distance(stations, p)
assert len(distance_list) == len(stations)
assert distance_list[0][0].name == "Cambridge Jesus Lock"

def test_stations_within_radius(): 
     stations = build_station_list()
     p = (52.2053, 0.1218)
     radius = 10
     stations_within_radius = [s for s in stations if haversine(p, s.coord) < radius]
assert len(stations_within_radius) > 0
assert any(s.name == "Cambridge Jesus Lock" for s in stations_within_radius)