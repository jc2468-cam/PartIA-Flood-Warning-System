"""Unit test for the flood module"""

from floodsystem.flood import stations_highest_rel_level


def dummy_stations():
    s1 = MonitoringStation("http://example.com/id/stations/1", "http://example.com/id/measures/1", "Station 1", (0,0), (0.1,0.0), "River 1", "Town 1")
    s2 = MonitoringStation("http://example.com/id/stations/2", "http://example.com/id/measures/2", "Station 2", (0,30), (0.5,1.0), "River 1", "Town 2")
    s3 = MonitoringStation("http://example.com/id/stations/3", "http://example.com/id/measures/3", "Station 3", (30,30), (0.2,0.3), "River 2", "Town 3")
    s3 = MonitoringStation("http://example.com/id/stations/3", "http://example.com/id/measures/3", "Station 3", (40,30), None, "River 3", "Town 3")
    s1.latest_level, s2.latest_level, s3.latest_level, s4.latest_level = 0.2, 0.4, None, 0.4
    return [s1, s2, s3]
