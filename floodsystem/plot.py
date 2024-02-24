"""
This module contains functions for plotting water level data over time for monitoring stations.
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime

from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit


def plot_water_level_with_fit(station, dates, levels, p):
    """
    Plots the recent water levels for a station, as well as the fitted polynomial and typical level ranges.

    If Stations have typical ranges, the typical level range lines are not plotted

    # Inputs
    - `station`: the station to plot values for.
    - `dates`: the dates and times at which the levels were recorded.
    - `levels`: the water levels recorded at the monitoring station.
    - `p`: the degree of polynomial to fit the the station's water level data.
    """
    # Create the plot
    fig, ax = plt.subplots()

    # Plot the water levels over time
    ax.plot(dates, levels, linewidth=2.0, label="Measured")

    # Fit polynomial to level data
    offset, polynomial = polyfit(dates, levels, p)
    # Create offset dates for inputs to the polynomial
    date_array = np.array(dates)
    date_array -= offset
    # Create predicted water levels form polynomial fit
    predicted = polynomial(date_array)

    ax.plot(dates, predicted, linewidth=1.5, color="yellow", label="Predicted")

    # Add typical range lines if the range is consistent
    if station.typical_range_consistent():
        ax.plot([dates[0], dates[-1]], [station.typical_range[0]]*2, linewidth=1.0, color="grey")
        ax.plot([dates[0], dates[-1]], [station.typical_range[1]]*2, linewidth=1.0, color="grey")

    ax.set_xlabel("time")
    ax.set_ylabel("water level / m")

    ax.legend()

    plt.show()
