from floodsystem import geo
from floodsystem.stationdata import build_station_list

stations = build_station_list()

output = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)

print (output)