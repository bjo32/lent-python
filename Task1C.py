from floodsystem import geo
from floodsystem.utils import sort_by_key
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    output = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    output = sort_by_key(output, 0, reverse=False)
    print(output)

if __name__ == "__main__":
    run()