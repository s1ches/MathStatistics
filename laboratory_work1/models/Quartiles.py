from constants import round_digits_count


class Quartiles:
    def __init__(self,
                 first_quantile: float | None = None,
                 second_quantile: float | None = None,
                 third_quantile: float | None = None):
        self.first_quantile: float | None = first_quantile
        self.second_quantile: float | None = second_quantile
        self.third_quantile: float | None = third_quantile

    def __str__(self) -> str:
        return (f'Квантили(1/4, 1/2, 1/4): '
                f'{self.first_quantile.__round__(round_digits_count)}\t'
                f'{self.second_quantile.__round__(round_digits_count)}\t'
                f'{self.third_quantile.__round__(round_digits_count)}')
