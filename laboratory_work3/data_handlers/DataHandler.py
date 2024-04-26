import numpy as np
from models.DataModel import DataModel


def handle_data(data: DataModel) -> DataModel:
    # Ковариация(коэффициентом корреляции(r))
    data.correlation_coefficient = ((1 / len(data.x_sample))
                                    * sum((data.x_sample - data.x_mean) * (data.y_sample - data.y_mean))
                                    / (data.x_std * data.y_std))

    # Коэффициент регрессии
    data.regression_coefficient = data.correlation_coefficient * data.x_std / data.y_std

    data.x_prediction = get_prediction(data.x_mean, data.regression_coefficient, data.y_prediction, data.y_mean)

    return data


# Уравнение регрессии
def get_prediction(x_mean: float, regression_coefficient: float, y: np.ndarray | float, y_mean: float)\
        -> np.ndarray[float]:
    return x_mean + regression_coefficient * (y - y_mean)
