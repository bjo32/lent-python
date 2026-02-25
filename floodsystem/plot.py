
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """
    Task 2E: Plots the water level data and typical range for a given station.
    """
    # Plot the actual water level data over time
    plt.plot(dates, levels, label="Water Level")
    
    low, high = station.typical_range
    # Add horizontal lines for typical low and high levels
    plt.axhline(y=low, color='r', linestyle='--', label="Typical Low")
    plt.axhline(y=high, color='g', linestyle='--', label="Typical High")
        
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    
    # Rotate the date labels on the x-axis so they don't overlap
    plt.xticks(rotation=45)
    
    plt.title(station.name)
    plt.legend()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """
    Task 2F: Plots the water level data, typical range, and a polynomial fit of degree p.
    """
    # 1. Get the polynomial object and the time shift 
    poly, d0 = polyfit(dates, levels, p)
    
    # 2. Plot the original data as discrete points (scatter plot)
    plt.plot(dates, levels, '.', label="Raw Data")
    
    # 3. Generate continuous points for a smooth fitted curve
    x = matplotlib.dates.date2num(dates)
    x_shifted = x - d0
    # Generate 30 evenly spaced points between the first and last day
    x_vals = np.linspace(x_shifted[0], x_shifted[-1], 30)
    
    # Plot the fitted curve. convert numeric dates back to datetime for the x-axis
    plt.plot(matplotlib.dates.num2date(x_vals + d0), poly(x_vals), color='orange', label=f"Polynomial Fit (Degree {p})")
    
    # 4. Add typical range horizontal lines
    low, high = station.typical_range
    plt.axhline(y=low, color='r', linestyle='--', label="Typical Low")
    plt.axhline(y=high, color='g', linestyle='--', label="Typical High")
        
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(f"{station.name} (Data Fit)")
    plt.legend()
    plt.show()
