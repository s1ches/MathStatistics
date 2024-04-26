import numpy as np

from constants import y_prediction, round_digits


class DataModel:
    def __init__(self, x_sample: np.ndarray[float], y_sample: np.ndarray[float]):
        self.x_sample = x_sample
        self.y_sample = y_sample
        self.x_mean = np.mean(self.x_sample)
        self.x_std = np.std(self.x_sample)
        self.y_mean = np.mean(self.y_sample)
        self.y_std = np.std(self.y_sample)
        self.correlation_coefficient = 0
        self.regression_coefficient = 0
        self.y_prediction = y_prediction
        self.x_prediction = 0

    def __str__(self):
        return (f"Samples:\n"
                f"X sample:\n {self.x_sample}\n\n"
                f"Y sample:\n {self.y_sample}\n\n"
                f"Means:\n"
                f"X mean: {self.x_mean.__round__(round_digits)}\n"
                f"Y mean: {self.y_mean.__round__(round_digits)}\n\n"
                f"Mean Standard Deviation:\n"
                f"X standard deviation: {self.x_std.__round__(round_digits)}\n"
                f"Y standard deviation: {self.y_std.__round__(round_digits)}\n\n"
                f"Correlation coefficient: {self.correlation_coefficient.__round__(round_digits)}\n\n"
                f"Regression coefficient: {self.regression_coefficient.__round__(round_digits)}\n\n"
                f"Predictions:\n"
                f"X Prediction: {self.x_prediction.__round__(round_digits)}\n"
                f"Y Prediction: {self.y_prediction}\n\n")
