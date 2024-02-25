"""
This module contains functions related to predicting the risk of flooding at monitoring stations.
"""
from floodsystem.datafetcher import fetch_measure_levels
import datetime

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

def get_all_town_risk_levels(stations, n, p):
    """
    Returns the assessed risk of all towns given its stations' water level history.

    # Inputs
    - `stations`: a `list` of all stations.
    - `n`: the number of days to fetch latest measure levels from.
    - `p`: the degree of the polynomial used internally to fit to the data.

    """
    towns = [list(), list(), list(), list()]
    severities = dict()
    for station in stations:
        if station.town != None:
            if station.typical_range_consistent() == False:
                risk = 2
            else:
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=n))
                risk = get_risk_level(dates, levels, p)
            if not station.town in severities:
                severities[station.town] = [0]*4
            severities[station.town][risk] += 1

    for town, risks in severities.items():
        current_risk = 3
        if risks[2] > 0:
            current_risk = 2
            if risks[2] > 1:
                risks[1] += 1
        if risks[1] > 0:
            current_risk = 1
            if risks[1] > 1:
                risks[0] += 1
        if risks[0] > 0:
            current_risk = 0
        towns[current_risk] += town 

    return towns
