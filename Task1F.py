from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_station_number
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

def run():
    """Requirements for Task F"""

    # Build list of stations
    stations = build_station_list()#

    # Sorting the list of stations with inconsistent data in alphabetical order
    print(sorted([s.name for s in  inconsistent_typical_range_stations(stations)]))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()