from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_station_number

N = 14

def run():
    """Requirements for Task E"""

    # Build list of stations
    stations = build_station_list()

    # Getting a list of N river names with the number of stations on them,
    # sorted in descending order, including any more rivers with the same
    # number of station as the Nth river
    print(rivers_station_number(stations, N))




if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()