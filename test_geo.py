"""Unit test for the geo module"""

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, haversine, rivers_station_number

from math import pi


def dummy_stations():
    s1 = MonitoringStation("http://example.com/id/stations/1", "http://example.com/id/measures/1", "Station 1", (0,0), (0.1,0.2), "River 1", "Town 1")
    s2 = MonitoringStation("http://example.com/id/stations/2", "http://example.com/id/measures/2", "Station 2", (0,30), (0.2,0.3), "River 1", "Town 2")
    s3 = MonitoringStation("http://example.com/id/stations/3", "http://example.com/id/measures/3", "Station 3", (30,30), (0.3,0.4), "River 2", "Town 3")
    return [s1, s2, s3]

def test_haversine():
    # Tests if the calculated distance between each pair of points is within 10 m of the expected distance.
    assert abs(haversine((0, 0), (180, 0)) - (pi * 6371)) < 0.01
    assert abs(haversine((0, 0), (90, 0)) - (pi * 6371 / 2)) < 0.01
    assert abs(haversine((0, 0), (0, 90)) - (pi * 6371 / 2)) < 0.01
    assert abs(haversine((0, 0), (18.31, 90)) - (pi * 6371 / 2)) < 0.01

def test_stations_by_distance():
    # Get dummy stations
    stations = dummy_stations()

    # Sort dummy stations
    sorted_stations = stations_by_distance(stations, (0,90))

    assert [pair[0].name for pair in sorted_stations] == ["Station 2", "Station 3", "Station 1"]

def test_stations_within_radius():
    # Get dummy stations
    stations = dummy_stations()

    # Get stations with 3,500 km of (0,0)
    near_stations = stations_within_radius(stations, (0,0), 3500)

    assert [station.name for station in near_stations] == ["Station 1", "Station 2"]

def test_rivers_with_station():
    # Get dummy stations
    stations = dummy_stations()

    # Get all rivers
    rivers = rivers_with_station(stations)

    assert set(rivers) == set(["River 1", "River 2"])

def test_stations_by_river():
    # Get dummy stations
    stations = dummy_stations()

    # Get stations on each river
    station_map = stations_by_river(stations)

    assert sum([station.name in ["Station 1", "Station 2"] for station in station_map["River 1"]]) == 2
    assert [station.name for station in station_map["River 2"]] == ["Station 3"]

def test_rivers_station_number():
    # Get dummy stations
    stations = dummy_stations()

    assert (rivers_station_number(stations, 1) == ([('River 1', 2)]))
    assert (rivers_station_number(stations, 2) == ([('River 1', 2), ('River 2', 1)]))
