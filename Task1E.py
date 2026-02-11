
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list()

    N = 9
    top_rivers = rivers_by_station_number(stations, N)

    print(f"Top {N} rivers by station count:")
    print(top_rivers)

if __name__ == "__main__":
    run()
