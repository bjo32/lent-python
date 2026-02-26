from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import town_flood_warnings


stations = build_station_list()
update_water_levels(stations)
print(town_flood_warnings(stations))