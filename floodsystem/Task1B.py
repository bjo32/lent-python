from floodsystem import geo
from geo import stations_by_distance
from floodsystem.stationdata import build_station_list
stations = build_station_list()

""" these two functions take the list of stations orderd by distance and appends the first/last 10 entries
 then appends them to a new list."""
def closest_10_stations(stations, p): 
    list_of_stations = []
    for i in range(9):
      list_of_stations.append(geo.stations_by_distance(stations, p)[i])
    return list_of_stations

def furthest_10_stations(stations, p):
    list_of_stations = []
    for i in range(1,10):
        list_of_stations.append(geo.stations_by_distance(stations, p)[-i])
    return list_of_stations
    
"""to test:"""
print(closest_10_stations(stations, (52.2053, 0.1218)))
print(furthest_10_stations(stations, (52.2053, 0.1218)))