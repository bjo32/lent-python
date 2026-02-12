
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()

    inconsistent_list = inconsistent_typical_range_stations(stations)
    
    names = [s.name for s in inconsistent_list]
    names.sort()
    
    print(names)

if __name__ == "__main__":
    run()
