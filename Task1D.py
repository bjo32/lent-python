
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation

def test_1d():
    stations = [
        MonitoringStation("sta1", "m1","s1",(0, 0), (0, 1), "River Cam", "Town1"),
        MonitoringStation("sta1", "m2","s2",(0, 0), (0, 1), "River Cam", "Town2"),
        MonitoringStation("sta3", "m3","s3",(0, 0), (0, 1), "River Thames", "Town3")]
    
    
    def test_rivers_with_station():
        rivers = rivers_with_station(stations)
        assert len(rivers) == 2
        assert rivers == {"River Cam", "River Thames"}
    
    def test_stations_by_river():
        river_map = stations_by_river(stations)
        assert len(river_map["River Cam"]) == 2
        assert len(river_map["River Thames"]) == 1




def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(f"{len(rivers)} stations. First 10 - {sorted(list(rivers))[:10]}")


    river_map = stations_by_river(stations)
    rivers_to_check = ['River Aire', 'River Cam', 'River Thames']
    
    for river in rivers_to_check:

        stations_on_river = river_map[river]    #get the list of station objects for specific river
        
        station_names = [s.name for s in stations_on_river]     #extract the name attribute
        station_names.sort()
        print(f"Stations on {river}: {station_names}")

if __name__ == "__main__":      #check if the script is being run directly
    run()
