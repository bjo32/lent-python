
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
def test_1f():

    
    s_good = MonitoringStation("Good", "River X", (1.0, 2.0))
    
    s_bad_logic = MonitoringStation("Bad Logic", "River X", (2.0, 1.0))  # Inconsistent station
    
    # Inconsistent station with None data
    s_bad_none = MonitoringStation("Bad None", "River X", None)
    
    # Partial None
    s_bad_partial = MonitoringStation("Bad Partial", "River X", (1.0, None))

    stations = [s_good, s_bad_logic, s_bad_none, s_bad_partial]
    assert s_good.typical_range_consistent() == True
    assert s_bad_logic.typical_range_consistent() == False
    assert s_bad_none.typical_range_consistent() == False


def run():

    stations = build_station_list()

    inconsistent_list = inconsistent_typical_range_stations(stations)
    
    names = [s.name for s in inconsistent_list]
    names.sort()
    
    print(names)

if __name__ == "__main__":
    run()
