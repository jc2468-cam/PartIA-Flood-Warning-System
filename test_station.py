# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from test_geo import dummy_stations
from test_flood import dummy_stations as dummy_stations_latest


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
     # Get dummy stations
    stations = dummy_stations()

    assert (stations[0].typical_range_consistent() == False)
    assert (stations[1].typical_range_consistent() == True)
    assert (stations[2].typical_range_consistent() == False)

def test_inconsistent_typical_range_stations():
     # Get dummy stations
    stations = dummy_stations()

    assert inconsistent_typical_range_stations(stations) == [stations[0], stations[2]]

def test_relative_water_level():
     # Get dummy stations
    stations = dummy_stations_latest()

    assert stations[0].relative_water_level() == None
    assert round(stations[1].relative_water_level(), 5) == -0.2
    assert stations[2].relative_water_level() == None
    assert round(stations[3].relative_water_level(), 5) == 1.2
    assert stations[4].relative_water_level() == None
