from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


# Latitude and longitude of Cambridge city centre
CITY_CENTRE = (52.2053, 0.1218)


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Sort stations by distance from Cambridge city centre
    sorted_stations = stations_by_distance(stations, CITY_CENTRE)

    # Print nearest stations and their distances
    print([(s[0].name, s[0].town, s[1]) for s in sorted_stations[:10]])

    # Print farthest stations and their distances
    print([(s[0].name, s[0].town, s[1]) for s in sorted_stations[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
