import numpy as np
from numpy import ndarray
from models.Quartiles import Quartiles
from constants import *


class DataInfo:
    def __init__(self):
        self.variation_series: ndarray[float] = np.array(0)
        self.sample_size: int = 0
        self.mean: float = 0.0
        self.median: float = 0.0
        self.avg_absolute_deviation: float = 0.0
        self.displaced_dispersion: float = 0.0
        self.no_displaced_dispersion: float = 0.0
        self.quartiles: Quartiles = Quartiles()
        self.min_value: float = 0.0
        self.max_value: float = 0.0
        self.spread: float = 0.0
        self.standard_deviation: float = 0.0
        self.asymmetry_coefficient: float = 0.0

    def __str__(self):
        return (f'Информация о выборке\n'
                f'Объём выборки: {self.sample_size}\n\n'
                f'Среднее по выборке: {self.mean.__round__(round_digits_count)}\n'
                f'Медиана: {self.median.__round__(round_digits_count)}\n\n'
                f'Дисперсия(с отклонением): {self.no_displaced_dispersion.__round__(round_digits_count)}\n'
                f'Дисперсия(без отклонения): {self.displaced_dispersion.__round__(round_digits_count)}\n'
                f'Стандартное отклонение: {self.standard_deviation.__round__(round_digits_count)}\n'
                f'Среднее абсолютное отклонение: {self.avg_absolute_deviation.__round__(round_digits_count)}\n\n'
                f'Квантили(1/4, 1/2, 1/4): '
                f'{self.quartiles.first_quantile.__round__(round_digits_count)}\t'
                f' {self.quartiles.second_quantile.__round__(round_digits_count)}\t'
                f' {self.quartiles.third_quantile.__round__(round_digits_count)}\n\n'
                f'Минимальное значение: {self.min_value.__round__(round_digits_count)}\t'
                f' Максимальное значение: {self.max_value.__round__(round_digits_count)}\n'
                f'Разброс: {self.spread.__round__(round_digits_count)}\n\n'
                f'Коэффициент асимметрии: {self.asymmetry_coefficient.__round__(round_digits_count)}')
