import numpy as np
from numpy import ndarray
from models.DataInfo import DataInfo
from models.Quartiles import Quartiles


def handle_data(data: ndarray[float]) -> DataInfo:
    info: DataInfo = DataInfo()

    # Sample size
    n: int = data.size
    info.sample_size = n

    # Get the variation series
    data: ndarray[float] = np.sort(data)
    info.variation_series = data

    # Get the average of the series
    mean: float = sum(data) / n
    info.mean = mean

    # Get the median
    median: float = data[n // 2] if n % 2 != 0 else (data[(n - 1) // 2] + data[(n + 1) // 2]) / 2
    info.median = median

    # Get the mode
    mode: ndarray[float] = get_mode(data)
    info.mode = mode

    # Get the average absolute deviation
    avg_absolute_deviation: float = sum(abs(data_item - mean) for data_item in data) / n
    info.avg_absolute_deviation = avg_absolute_deviation

    # Get the dispersion
    # displaced
    displaced_dispersion: float = sum((data_item - mean)**2 for data_item in data) / n
    info.displaced_dispersion = displaced_dispersion

    # no displaced
    no_displaced_dispersion: float = sum((data_item - mean)**2 for data_item in data) / (n - 1)
    info.no_displaced_dispersion = no_displaced_dispersion

    # Get the spread
    min_value: float = data[0]
    info.min_value = min_value

    max_value: float = data[data.size - 1]
    info.max_value = max_value

    spread: float = max_value - min_value
    info.spread = spread

    # Get the standard deviation
    standard_deviation: float = displaced_dispersion ** 0.5
    info.standard_deviation = standard_deviation

    # Get the Base Quantiles(Q(25%), Q(50%), Q(75%))
    quartiles: Quartiles = Quartiles()

    # Q(25%)
    quartiles.first_quantile = data[n // 4] if n % 4 != 0 else (data[n // 4 + 1] + data[n // 4]) / 2

    # Median/Q(50%)
    quartiles.second_quantile = median

    # Q(75%)
    quartiles.third_quantile = data[(3 * n) // 4] if n % 4 != 0 else (data[(3 * n) // 4 + 1] + data[(3 * n) // 4]) / 2

    info.quartiles = quartiles

    # Get the inter-quartile latitude
    inter_quartile_latitude = quartiles.third_quantile - quartiles.first_quantile
    info.inter_quartile_latitude = inter_quartile_latitude

    asymmetry_coefficient: float = sum((data_item - mean) ** 3 for data_item in data) / (n * standard_deviation ** 3)
    info.asymmetry_coefficient = asymmetry_coefficient

    return info


def get_mode(data: ndarray[float]) -> ndarray[float] | None:
    values, counts = np.unique(data, return_counts=True)

    if len(values) == len(data):
        return None

    mode_indexes = np.argwhere(counts == np.max(counts))

    return values[mode_indexes].flatten()
