import pandas as pd
import numpy as np
from models.DataModel import DataModel


def get_data(filepath: str) -> DataModel:
    # Read data from .cvs file
    df = pd.read_csv(filepath)

    # Convert data from data frame to NumPy Array
    return DataModel(np.array(df['X']), np.array(df['Y']))
