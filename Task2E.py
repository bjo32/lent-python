import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level 

def run():
    """
    Plots water levels over the past 10 days for the 5 stations at highest risk.
    """
    # Build stations and update real-time levels
    stations = build_station_list()
    update_water_levels(stations)

    top_5_stations = stations_highest_rel_level(stations, 5)
    
    # data for the past 10 days
    dt = 10 
    
    # Loop through the top 5 stations
    for station, rel_level in top_5_stations: 
        # Fetch historical dates and levels)
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        if len(dates) > 0 and len(levels) > 0:
            print(f"Plotting water levels for {station.name}:")
            plot_water_levels(station, dates, levels)
        else:
            print(f"No historical data available for {station.name}.")

if __name__ == "__main__":
    run()

