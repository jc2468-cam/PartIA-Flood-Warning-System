# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from math import sqrt, cos, sin, asin, pi, radians

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """
    Sorts a `list` of stations by the geographical distance from a given point.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s to sort.
    - `p`: a latitude and longitude pair to calculate the distances from.

    # Returns
    A `list` of `MonitoringStation`s sorted in ascending order by distance from point `p`.
    """
    return sorted([(station, haversine(station.coord, p)) for station in stations], key = lambda x: x[1])


def stations_within_radius(stations, centre, r):
    """
    Filters a `list` of `MonitoringStation`s, returning ones which are within specified radius of geographic coordinate.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s to filter.
    - `centre`: the (latitude, longitude) pair which the monitoring stations must be within the specified radius of.
    - `r`: the maximum distance a monitoring station can be from `centre`
    """
    return [station for station in stations if haversine(station.coord, centre) <= r]


def rivers_with_station(stations):
    """
    Gets all of the rivers on which a `list` of `MonitoringStation`s are located.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s.

    # Returns
    A `list` containing the names of all the rivers on which a station in `stations` was located.

    A list is returned so that the result can be ordered.
    """
    return list({station.river for station in stations})


def stations_by_river(stations):
    """
    Creates a `dict` mapping all of the rivers on which a `MonitoringStation` in `list` is located to the `MonitoringStation`s on that river.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s.

    # Returns
    A `dict` mapping river names to `list`s of stations on that river.
    """
    out = dict()
    for station in stations:
        if station.river in out:
            out[station.river] += [station]
        else:
            out[station.river] = [station]
    return out


def haversine(p1, p2):
    """
    Computes the great circle distance between 2 points on the earth using the haversine formula.

    # Inputs
    - `p1` & `p2`: A pair of (longitude, latitude) coordinates to calculate the distance between.

    # Returns
    The distance in km over the surface of the earth between `p1` and `p2`, assuming the earth is a perfect sphere of radius 6371 km.
    """
    p1, p2 = [radians(e) for e in p1], [radians(e) for e in p2]
    return 12742 * asin(sqrt(sin(0.5 * (p1[0] - p2[0]))**2 + cos(p1[0])*cos(p2[0])*sin(0.5 * (p1[1] - p2[1]))**2))


def rivers_station_number(stations, N):
    """
    Determining the `N` number of rivers with the greatest number of `MonitoringStation`s.

    # Inputs
    - `stations`: a `list` of `MonitoringStation`s
    - `N`: number of rivers with greatest number of `MonitoringStation`s

    # Returns
    A list of `N` river name and number of station tuples, sorted by the number of stations.
    If there are more rivers with the same number of stations as the Nth entry, they are also included in the list.
    """
    # Creating a dict of river name key and stations on river list value
    river_stations = stations_by_river(stations)

    # Getting a list of river name and number of stations on that river tuple
    river_n_stations = list()
    for river, stas in river_stations.items():
        a = river
        b = len(stas)
        river_n_stations += [(a, b)]

    # Sorting the list in descending order of river numbers
    sorted_river_n_stations = sorted(river_n_stations, key = lambda x: x[1], reverse = True)

    # Checking if any more rivers have the same number of stations as the Nth river
    counter = 0
    while counter < 1500: # Max number of river with station was 1022
        counter += 1
        try:
            i = sorted_river_n_stations[N-1]
            j = sorted_river_n_stations[N]
            if i[1] == j[1]: 
                N += 1
            else:
                break
        except:
            break


    return sorted_river_n_stations[:N]
