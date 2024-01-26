from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


# Rivers to print stations on
RIVERS = ["River Aire", "River Cam", "River Thames"]


def run():
    """Requirements for Task D"""

    # Build list of stations
    stations = build_station_list()

    # Get all the rivers which have a station
    rivers = rivers_with_station(stations)

    # Sort the river names into alphabetical order
    rivers.sort()

    # Print the first 10 river names
    print(f"{len(rivers)} rivers. First 10 - {rivers[:10]}")


    # Get a map of rivers to stations
    river_map = stations_by_river(stations)

    for river in RIVERS:
        print(f"Stations on {river}: {sorted([station.name for station in river_map[river]])}")


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
