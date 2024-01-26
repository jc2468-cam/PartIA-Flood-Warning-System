from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


# Latitude and longitude of Cambridge city centre
CITY_CENTRE = (52.2053, 0.1218)


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Filter stations, keeping those within 10 km of Cambridge city centre
    near_stations = stations_within_radius(stations, CITY_CENTRE, 10)

    # Get the names of all the nearby stations
    station_names = [station.name for station in near_stations]

    # Sort the station names into alphabetical order
    station_names.sort()

    # Print the alphabetically ordered station names
    print(station_names)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
