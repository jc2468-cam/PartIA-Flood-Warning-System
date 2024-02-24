import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels


def run():

    # Build list of stations
    stations = build_station_list()

    # Ploting the water levels over the past 10 days
    # for the 5 stations with the highest current relative water level
    for station in stations_highest_rel_level(stations, 5)[1:]:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        print(len(dates))
        print(len(levels))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
