"""
This module contains functions related to predicting the water levels for monitoring stations.
"""

import numpy as np

from matplotlib.dates import date2num


def polyfit(dates, levels, p):
    """
    Computes the least-squares fit for a degree `p` polynomial to the level history data of a station

    # Inputs
    - `dates`: a `list` of the dates of the measurements.
    - `levels`: the water level measurements.
    - `p`: the degree of the polynomial to fit to the data.

    # Returns
    A `tuple` containing a 0-offset for the dates and the fitted polynomial.
    """
    # Convert dates to a numerical representation
    date_array = date2num(dates)
    # Offset the dates to have smaller values to avoid floating point errors
    offset = date_array[0]
    date_array -= offset

    # Replaces `None` with the previous recorded value (or 1 if the first value is missing), allowing fitting to stations with partially missing data
    for i in range(len(levels)):
        if levels[i] == None:
            if i == 0:
                levels[i] == 1.
            else:
                levels[i] = levels[i-1]

    # Get polynomial coefficients
    coefficients = np.polyfit(date_array, levels, p)

    # Convert coefficient into a polynomial object
    polynomial = np.poly1d(coefficients)

    return (offset, polynomial)
