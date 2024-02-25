"""
This module contains functions related to predicting the risk of flooding at monitoring stations.
"""

import numpy as np

from matplotlib.dates import date2num


def stations_level_over_threshold(stations, tol):
    """
    Returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol
    and (ii) the relative water level at the station.
    The returned list is sorted by the relative level in descending order.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s to sort.
    - `tol`: the minimum relative water level.

    """
    over_threshold = list()
    # Getting a list of station name and latest relative water level over tol
    for station in stations:
        a = station.name
        b = station.relative_water_level()
        if b != None and b > tol and station.typical_range_consistent():
            over_threshold += [(a, b)]
    
    # Sorting the list in descending order of relative level
    return sorted(over_threshold, key = lambda x: x[1], reverse = True)


def stations_highest_rel_level(stations, N):
    """
    Returns a `list` of the first `N` stations with the highest relative water level, sorted by their relative water levels.

    If Stations have inconsistent water levels, then they will by put to the end of the list, and only returned after all stations with consistent water levels,
    even if these water levels are negative.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s to sort.
    - `N`: the maximum number of stations to return.

    # Returns
    A `list` of `MonitoringStation`s sorted in descending order by relative water level.
    """
    return sorted(stations, key = lambda s: s.relative_water_level() if s.relative_water_level() != None else float("-inf"), reverse=True)[:N]

def get_risk_level(dates, levels, p):
    """
    Returns the assessed risk of a station given its water level history.

    If Stations have inconsistent water levels, then they will by put to the end of the list, and only returned after all stations with consistent water levels,
    even if these water levels are negative.

    # Inputs
    - `dates`: a `list` of the dates of the measurements.
    - `levels`: the water level measurements.
    - `p`: the degree of the polynomial used internally to fit to the data.

    # Returns
    A numerical assessment of the risk level at the station.
    """
    # Create prediction polynomial
    polynomial, offset = polyfit(dates, levels, p)

    # Prediction of time until water level reaches critical values based on current trend
    coefficients = polynomial.polydir()
    derivative = np.poly1d(coefficients)(date2num(dates)[-1] - offset)
    days_to_top = (1.2 - levels[-1]) / derivative

    # There probably already is a flood: severe risk
    if level[-1] > 2:
        return 0
    else if derivative > 0:
        # River level is above typical range and rising: severe risk
        if days_to_top < 0:
            return 0
        # River level is below typical high, but will soon reach this value at current rise rate: high risk
        else if days_to_top < 1:
            return 1
        # River level is below typical high, but will reach this value fairly soon at current rise rate: moderate risk
        else if days_to_top < 7:
            return 2
        # River level is in normal range and only rising slowly: low risk
        else:
            return 3
    else:
        # River level is high and not falling very fast: high
        if days_to_top > 5:
            return 1
        # River is high and falling fairly fast: moderate
        else if days_to_top > 0:
            return 1
        # River is in normal range and falling: low risk
        else:
            return 3
