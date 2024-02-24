import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit


N = 5
DT = 10
ORDER = 3


def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    # Plot fitted polynomial for the `N` stations with the highest relative water levels
    for station in stations_highest_rel_level(stations, N):
        plot_water_level_with_fit(station, *fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=DT)), ORDER)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
