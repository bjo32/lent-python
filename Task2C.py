from floodsystem.datafetcher import fetch_station_data
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)
print(stations_highest_rel_level(stations, 10))