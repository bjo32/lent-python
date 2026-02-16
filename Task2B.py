from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    for station in stations:
        print(relative_water_level(station))
run()