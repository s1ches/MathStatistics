import constants
from numpy import ndarray
import numpy as np
from models.DataInfo import DataInfo


class PlotBuilderHelper:
    @staticmethod
    def configure_plot(axis, title: str, x_label: str, y_label: str) -> None:
        axis.set_title(title,
                       fontdict={'fontsize': constants.plot_title_font_size,
                                 'fontweight': 'bold', 'color': constants.plot_text_color})
        axis.set_xlabel(x_label,
                        fontdict={'fontsize': constants.plot_text_font_size, 'color': constants.plot_text_color})

        axis.set_ylabel(y_label,
                        fontdict={'fontsize': constants.plot_text_font_size, 'color': constants.plot_text_color})

    @staticmethod
    def get_elements_in_boundaries_probability(data: DataInfo, elements_in_boundaries_count: ndarray[float]) \
            -> ndarray[float]:
        result: list[float] = []

        for element in elements_in_boundaries_count:
            result.append(element / data.sample_size)

        return np.array(result)

    @staticmethod
    def get_boundaries(data: DataInfo, step: float, steps_count) -> ndarray[float]:
        result: list[float] = [data.variation_series[0] + step / 2]

        for i in range(1, steps_count - 2):
            result.append(result[i - 1] + step)

        result.append(result[len(result) - 1] + step)

        return np.array(result)

    @staticmethod
    def get_elements_count_in_boundaries(data: DataInfo, boundaries: ndarray[float]) -> ndarray[int]:
        result = []

        left_bound: float = float('-inf')
        right_bound: float = boundaries[0]

        result.append(PlotBuilderHelper.__get_elements_count_in_boundary(data, left_bound, right_bound))

        elements_counted: int = result[0]

        for i in range(boundaries.size - 1):
            left_bound = boundaries[i]
            right_bound = boundaries[i + 1]
            result.append(PlotBuilderHelper.__get_elements_count_in_boundary(data, left_bound, right_bound,
                                                                             elements_counted))
            elements_counted += result[len(result) - 1]

        left_bound: float = boundaries[boundaries.size - 1]
        right_bound: float = float('inf')
        result.append(PlotBuilderHelper.__get_elements_count_in_boundary(data, left_bound, right_bound,
                                                                         elements_counted))

        return np.array(result)

    @staticmethod
    def __get_elements_count_in_boundary(data: DataInfo, left_boundary: float, right_boundary: float,
                                         from_index: int = 0) -> int:
        result: int = 0

        for i in range(from_index, data.variation_series.size):
            if right_boundary > data.variation_series[i] >= left_boundary:
                result += 1
            else:
                break

        return result
