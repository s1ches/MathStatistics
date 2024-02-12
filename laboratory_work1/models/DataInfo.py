from numpy import ndarray
from models.Quartiles import Quartiles
from constants import round_digits_count


class DataInfo:
    def __init__(self):
        self.variation_series: ndarray[float] | None = None
        self.sample_size: int | None = None
        self.mean: float | None = None
        self.median: float | None = None
        self.avg_absolute_deviation: float | None = None
        self.displaced_dispersion: float | None = None
        self.no_displaced_dispersion: float | None = None
        self.quartiles: Quartiles | None = None
        self.min_value: float | None = None
        self.max_value: float | None = None
        self.spread: float | None = None
        self.standard_deviation: float | None = None
        self.asymmetry_coefficient: float | None = None
        self.inter_quartile_latitude: float | None = None
        self.mode: float | None = None

    def __str__(self) -> str:
        return (f'Информация о выборке\n'
                f'Объём выборки: {self.sample_size}\n\n'
                f'Среднее по выборке: {self.mean.__round__(round_digits_count)}\n'
                f'Медиана: {self.median.__round__(round_digits_count)}\n'
                f'Мода: {self.mode}\n\n'
                f'Дисперсия(с отклонением): {self.displaced_dispersion.__round__(round_digits_count)}\n'
                f'Дисперсия(без отклонения): {self.no_displaced_dispersion.__round__(round_digits_count)}\n'
                f'Стандартное отклонение: {self.standard_deviation.__round__(round_digits_count)}\n'
                f'Среднее абсолютное отклонение: {self.avg_absolute_deviation.__round__(round_digits_count)}\n\n'
                f'{self.quartiles}\n'
                f'Интерквартильная широта: {self.inter_quartile_latitude.__round__(round_digits_count)}\n\n'
                f'Минимальное значение: {self.min_value.__round__(round_digits_count)}\t'
                f' Максимальное значение: {self.max_value.__round__(round_digits_count)}\n'
                f'Размах: {self.spread.__round__(round_digits_count)}\n\n'
                f'Коэффициент асимметрии: {self.asymmetry_coefficient.__round__(round_digits_count)}')
