
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def test_1e():
    # River A: 3 stations
    # River B: 2 stations
    # River C: 2 stations
    # River D: 1 stations
    stations = [
        DummyStation("S1", "River A", None), DummyStation("S2", "River A", None), DummyStation("S3", "River A", None),
        DummyStation("S4", "River B", None), DummyStation("S5", "River B", None),
        DummyStation("S6", "River C", None), DummyStation("S7", "River C", None),
        DummyStation("S8", "River D", None)
    ]
    top_1 = rivers_by_station_number(stations, 1)
    assert top_1[0][0] == "River A"
    assert len(top_1) == 1

    top_2 = rivers_by_station_number(stations, 2)
    assert len(top_2) == 3
    assert top_2[0][0] == "River A"
    
    # Check if River B and River C are present
    river_names = [x[0] for x in top_2]
    assert "River B" in river_names
    assert "River C" in river_names


def run():
    stations = build_station_list()

    N = 9
    top_rivers = rivers_by_station_number(stations, N)

    print(f"Top {N} rivers by station count:")
    print(top_rivers)

if __name__ == "__main__":
    run()

