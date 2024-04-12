import numpy as np
from constants import confidence_probability
from scipy import stats


def get_lower_confidence_limit_for_variance(data: np.ndarray[float]) -> float:
    data = np.sort(data)

    n = len(data)

    mean = np.sum(data) / n

    displaced_dispersion: float = np.sum((data - mean)**2) / n

    alpha = confidence_probability

    return n / stats.chi2.ppf(alpha, n - 1) * displaced_dispersion
