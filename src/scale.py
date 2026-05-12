"""
Utility module for feature scaling.

NOTE FOR EXAM (Task 2): One function in this file contains a bug.
The output it produces is in the range [-1, 0] instead of [0, 1].
Find it, fix it, and add a one-line comment above your fix explaining
what was wrong.
"""
import numpy as np
import pandas as pd


def min_max_scale(values):
    """
    Apply Min-Max scaling to a 1D array or pandas Series.
    Should return values in the range [0, 1].
    
    Formula (from class):
        x_scaled = (x - x_min) / (x_max - x_min)
    
    Parameters
    ----------
    values : array-like
        Numeric values to scale.
    
    Returns
    -------
    np.ndarray
        Scaled values, expected in [0, 1].
    """
    arr = np.asarray(values, dtype=float)
    col_min = arr.min()
    col_max = arr.max()
    # BUG (do not delete this comment until you fix the line below):
    return (arr - col_max) / (col_max - col_min)


def standardize(values):
    """
    Standardize a 1D array to zero mean, unit variance.
    This function is correct — do not modify.
    """
    arr = np.asarray(values, dtype=float)
    return (arr - arr.mean()) / arr.std()
