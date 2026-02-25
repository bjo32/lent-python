import datetime
import numpy as np
from floodsystem.analysis import polyfit

class DummyStation:
    def __init__(self, name, typical_range):
        self.name = name
        self.typical_range = typical_range

def test_polyfit():
    d1 = datetime.datetime(2026, 1, 1)
    d2 = datetime.datetime(2026, 1, 2)
    d3 = datetime.datetime(2026, 1, 3)
    dates = [d1, d2, d3]
    
    # Create linear water levels (y = 1.0 * x + 1.0)
    levels = [1.0, 2.0, 3.0]
    
    # Fit a 1st degree polynomial (a straight line)

    poly, d0 = polyfit(dates, levels, 1)
    
    # Day 0 (shifted to 0) should equal 1.0
    assert round(poly(0.0), 1) == 1.0
    
    # Day 2 (shifted to 2.0) should equal 3.0
    assert round(poly(2.0), 1) == 3.0
    

if __name__ == "__main__":
    test_polyfit()
