from floodsystem.station import MonitoringStation

     # Create a station
s_id = "test-s-id"    
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4)
river = "test river"
town = "Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
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