
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level 

def run():
    """
    Plots water levels and a degree 4 polynomial fit over the past 2 days for the 5 stations at highest risk.
    """
    # 1. Build stations and update real-time levels
    stations = build_station_list()
    update_water_levels(stations)
    
    # 2. Get the top 5 at-risk stations
    top_5_stations = stations_highest_rel_level(stations, 5)
    
    # We want data for the past 2 days for the polynomial fit
    dt = 2
    
    # Loop through the stations, fetch history, and plot with fit
    for station, rel_level in top_5_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        # Proceed only if we have enough data points to fit a degree 4 polynomial
        if len(dates) > 4 and len(levels) > 4:
            print(f"Plotting polynomial fit for {station.name}...")
            plot_water_level_with_fit(station, dates, levels, 4)
        else:
            print(f"Not enough historical data to fit a polynomial for {station.name}.")

if __name__ == "__main__":
    run()
