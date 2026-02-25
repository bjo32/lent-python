import numpy as np
import matplotlib.dates

def polyfit(dates, levels, p):
    """
    computes a least-squares fit of a polynomial of degree p to water level data.
    """
    
    #Convert datetime to float values(days since an epoch)
    x = matplotlib.dates.date2num(dates)
    
    d0 = x[0]
    x_shifted = x - d0
    
    #Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x_shifted, levels, p)
    
    #Convert the coefficients into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    
    return poly, d0

