import numpy as np
import matplotlib.dates

def polyfit(dates, levels, p):
    """
    computes a least-squares fit of a polynomial of degree p to water level data.
    """
    
    #Convert datetime objects to float values for matplotlib(days since an epoch)
    x = matplotlib.dates.date2num(dates)
    
    # to prevent numerical rounding errors with large numbers
    d0 = x[0]
    
    #Shift the x-axis, starts at x=0
    x_shifted = x - d0
    
    #Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x_shifted, levels, p)
    
    #Convert the coefficients into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    
    return poly, d0        #Returns a tuple of the polynomial object and the shift of the time axis.

