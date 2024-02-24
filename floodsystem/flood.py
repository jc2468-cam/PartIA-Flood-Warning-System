"""
This module contains functions related to predicting the risk of flooding at monitoring stations.
"""

def stations_highest_rel_level(stations, N):
    """
    Returns a `list` of the first `N` stations with the highest relative water level, sorted by their relative water levels.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s to sort.
    - `N`: the maximum number of stations to return.

    # Returns
    A `list` of `MonitoringStation`s sorted in descending order by relative water level.
    """
    return sorted(stations, key = lambda s: s.relative_water_level(), reverse=True)[:N]

