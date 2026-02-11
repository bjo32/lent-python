
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(f"{len(rivers)} stations. First 10 - {sorted(list(rivers))[:10]}")


    river_map = stations_by_river(stations)
    rivers_to_check = ['River Aire', 'River Cam', 'River Thames']
    
    for river in rivers_to_check:
        stations_on_river = river_map[river]
        
        station_names = [s.name for s in stations_on_river]
        station_names.sort()
        print(f"Stations on {river}: {station_names}")

if __name__ == "__main__":
    
    run()
