"""
This module contains functions related to predicting the water levels for monitoring stations.
"""

import numpy as np


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
    # Convert dates to an array, which implicitly converts to a numerical representation
    date_array = np.array(dates)
    # Offset the dates to have smaller values to avoid floating point errors
    date_array -= date_array[0]

    # Get polynomial coefficients
    coefficients = np.polyfit(date_array, levels, p)

    # Convert coefficient into a polynomial object
    polynomial = np.poly1d(coefficients)

    return (date_array[0], polynomial)
