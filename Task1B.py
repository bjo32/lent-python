from floodsystem import geo
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    distance_list = geo.stations_by_distance(stations, (52.2053, 0.1218))
    print(distance_list[0:9])
    print(distance_list[-10:])

if __name__ == "__main__":
    run()