import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
import numpy as np


def run():

    # Build list of stations
    stations = build_station_list()

    # Update water levels
    update_water_levels(stations)

    # Ploting the water levels over the past 10 days
    # for the 5 stations with the highest current relative water level

    for station in stations_highest_rel_level(stations, 5):
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
