from floodsystem import station
from floodsystem.stationdata import build_station_list
stations = build_station_list()

consistency = station.inconsistent_typical_range_stations(stations)
names = []
for i in consistency:
    names.append(i.name)
names.sort()
print("Stations with inconsistent typical range data:" + str(names))