from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    for station in stations:
        print(relative_water_level(station))
    print(stations_level_over_threshold(stations, 0.8))
    
run()

