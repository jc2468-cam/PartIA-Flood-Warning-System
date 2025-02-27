from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


N = 10


def run():
    """Requirements for Task C"""

    # Build list of stations
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    # Print the N stations with the highest relative water level
    print(*[f"{station.name} {station.relative_water_level()}" for station in stations_highest_rel_level(stations, N)], sep="\n")

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
