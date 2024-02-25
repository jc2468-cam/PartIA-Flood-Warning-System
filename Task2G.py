import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level, get_all_town_risk_levels

def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    towns = get_all_town_risk_levels(stations[:], 1, 3, True)

    print('=== Towns at severe risk of flooding ===')
    print(*towns[0], sep = '\n')
    print('\n'*3)
    print('=== Towns at high risk of flooding ===')
    print(*towns[1], sep = '\n')    
    print('\n'*3)
    print('=== Towns at moderate risk of flooding ===')
    print(*towns[2], sep = '\n')
    print('\n'*3)
    print('=== Towns at low risk of flooding ===')
    print(*towns[3], sep = '\n')    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
