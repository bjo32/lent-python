from floodsystem import  stationdata, station
from floodsystem.flood import stations_level_over_threshold

     # Create a station
s_id = "test-s-id"    
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4)
river = "test river"
town = "Town"
s = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
print(s)
print (s.relative_water_level())
s.latest_level = None
print (s.relative_water_level())
s.latest_level = -2.3
print( s.relative_water_level())
s.latest_level = 3.4
print(s.relative_water_level())
s.latest_level = 0.55
print(s.relative_water_level())

"""demonstrate the station class and its relative water level method."""
stations = stationdata.build_station_list()
stationdata.update_water_levels(stations)
print(stations_level_over_threshold(stations, 0.5))
