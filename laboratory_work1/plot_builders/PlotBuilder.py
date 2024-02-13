from models.DataInfo import DataInfo
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from numpy import ndarray
import numpy as np


class PlotBuilder:
    def __init__(self, data: DataInfo, plot_style: str | None = None):
        self.data: DataInfo = data
        self.plot_style: str | None = plot_style
        self.__steps_count: int = data.sample_size // 10
        self.__step: float = data.spread / (self.__steps_count - 1)

    def build_frequency_histogram(self) -> None:
        boundaries: ndarray[float] = self.__get_boundaries()

        elements_in_boundaries_count: ndarray[float] = self.__get_elements_count_in_boundaries(boundaries)

        figure, axis = plt.subplots()

        axis.grid(True)

        axis.add_patch(
            Rectangle((self.data.variation_series[0], 0),
                      self.__step, elements_in_boundaries_count[0]))

        boundary_index: int = 0
        for i in range(1, elements_in_boundaries_count.size - 1):
            axis.add_patch(
                Rectangle((boundaries[boundary_index], 0), self.__step, elements_in_boundaries_count[i]))

            boundary_index += 1

        axis.add_patch(
            Rectangle((boundaries[boundary_index], 0),
                      self.__step, elements_in_boundaries_count[elements_in_boundaries_count.size - 1]))

        axis.plot()
        plt.show()

    def build_probability_histogram(self) -> None:
        return None

    def build_distribution_function(self) -> None:
        return None

    def build_box_plot(self) -> None:
        return None

    def __get_boundaries(self) -> ndarray[float]:
        result: list[float] = [self.data.variation_series[0] + self.__step / 2]

        for i in range(1, self.__steps_count - 2):
            result.append(result[i - 1] + self.__step)

        result.append(result[len(result) - 1] + self.__step)

        return np.array(result)

    def __get_elements_count_in_boundaries(self, boundaries: ndarray[float]) -> ndarray[int]:
        result = []

        left_bound: float = float('-inf')
        right_bound: float = boundaries[0]

        result.append(self.__get_elements_count_in_boundary(left_bound, right_bound))

        elements_counted: int = result[0]

        for i in range(boundaries.size - 1):
            left_bound = boundaries[i]
            right_bound = boundaries[i + 1]
            result.append(self.__get_elements_count_in_boundary(left_bound, right_bound, elements_counted))
            elements_counted += result[len(result) - 1]

        left_bound: float = boundaries[boundaries.size - 1]
        right_bound: float = float('inf')
        result.append(self.__get_elements_count_in_boundary(left_bound, right_bound, elements_counted))

        return np.array(result)

    def __get_elements_count_in_boundary(self, left_boundary: float, right_boundary: float, from_index: int = 0) -> int:
        result: int = 0

        for i in range(from_index, self.data.variation_series.size):
            if right_boundary > self.data.variation_series[i] >= left_boundary:
                result += 1
            else:
                break

        return result
