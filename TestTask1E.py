from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number

N = 10

def run():
    """Requirements for Task E"""

    # Build list of stations
    stations = build_station_list()

    rivers_by_station_number(stations, N)




if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()