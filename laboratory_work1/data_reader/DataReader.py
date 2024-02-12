import pandas as pd
import numpy as np


def get_data(filepath: str) -> np.ndarray[float]:
    # Read data from .cvs file
    df = pd.read_csv(filepath)

    # Convert data from data frame to NumPy Array
    return np.array(df['X'])
