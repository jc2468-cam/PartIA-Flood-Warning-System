import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
