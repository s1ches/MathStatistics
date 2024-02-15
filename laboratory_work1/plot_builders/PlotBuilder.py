from models.DataInfo import DataInfo
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from numpy import ndarray
import numpy as np
import constants
from scipy.stats import norm


class PlotBuilder:
    def __init__(self, data: DataInfo, plot_style: str | None = None):
        self.data: DataInfo = data
        self.plot_style: str | None = plot_style
        self.__steps_count: int = data.sample_size // 10
        self.__step: float = data.spread / (self.__steps_count - 1)
        self.frequency_histogram_figure, self.frequency_histogram_axis = plt.subplots()
        self.probability_histogram_figure, self.probability_histogram_axis = plt.subplots()

    def build(self) -> None:
        plt.style.use(self.plot_style)

        self.__build_frequency_histogram()
        self.probability_histogram_axis.plot()

        self.__build_probability_histogram()
        self.probability_histogram_axis.plot()

        self.frequency_histogram_axis.legend(loc="upper left")
        self.probability_histogram_axis.legend(loc="upper left")
        plt.show()

    def __build_frequency_histogram(self) -> None:
        boundaries: ndarray[float] = self.__get_boundaries()

        elements_in_boundaries_count: ndarray[float] = self.__get_elements_count_in_boundaries(boundaries)

        self.__build_histogram(self.frequency_histogram_axis, boundaries, elements_in_boundaries_count)

        self.frequency_histogram_axis.plot()

        self.__build_data_info(self.frequency_histogram_axis, y_max=max(elements_in_boundaries_count) * 1.2)

        title: str = 'Частотная гистограмма'
        x_label: str = 'Данные'
        y_label: str = 'Частота'

        self.__configure_plot(self.frequency_histogram_axis, title, x_label, y_label)

    def __build_probability_histogram(self) -> None:
        boundaries: ndarray[float] = self.__get_boundaries()

        elements_in_boundaries_count: ndarray[float] = self.__get_elements_count_in_boundaries(boundaries)

        elements_in_boundaries_probability: ndarray[float] = \
            self.__get_elements_in_boundaries_probability(elements_in_boundaries_count)

        elements_in_boundaries_heights = elements_in_boundaries_probability / self.__step

        self.__build_histogram(self.probability_histogram_axis, boundaries, elements_in_boundaries_heights)

        self.__build_normal_distribution(self.probability_histogram_axis)

        self.__build_data_info(self.probability_histogram_axis, y_max=max(elements_in_boundaries_heights) * 1.2)

        title: str = 'Вероятностная гистограмма'
        x_label: str = 'Y'
        y_label: str = 'X'

        self.__configure_plot(self.probability_histogram_axis, title, x_label, y_label)

    def build_distribution_function(self) -> None:
        return

    def build_box_plot(self) -> None:
        return

    def __build_data_info(self, axis, y_max: float, y_min: float = 0) -> None:
        axis.vlines(x=self.data.quartiles.first_quantile, ymin=y_min, ymax=y_max, color='#f500d8',
                    label='Квантиль(1/4)')

        axis.vlines(x=self.data.median, ymin=y_min, ymax=y_max, color='blue', label='Медиана')

        axis.vlines(x=self.data.mean, ymin=y_min, ymax=y_max, color='#32a852', label='Мат. ожидание')

        axis.vlines(x=self.data.quartiles.third_quantile, ymin=y_min, ymax=y_max,
                    color='#f500d8', label='Квантиль(3/4)')

    def __build_normal_distribution(self, axis) -> None:
        normal_distribution_range: ndarray[float] = np.arange(self.data.min_value - 2 * self.__step,
                                                              self.data.max_value + 2 * self.__step, 0.001)

        axis.plot(normal_distribution_range,
                  norm.pdf(normal_distribution_range, self.data.mean,
                           self.data.standard_deviation),
                  color='red', label='Нормальное распределение')

    def __build_histogram(self, axis, boundaries: ndarray[float], columns_heights: ndarray[float]) -> None:
        axis.add_patch(
            Rectangle((self.data.variation_series[0], 0),
                      self.__step, columns_heights[0],
                      color=constants.plot_figure_color))

        boundary_index: int = 0
        for i in range(1, columns_heights.size - 1):
            axis.add_patch(
                Rectangle((boundaries[boundary_index], 0), self.__step,
                          columns_heights[i],
                          color=constants.plot_figure_color))

            boundary_index += 1

        axis.add_patch(
            Rectangle((boundaries[boundary_index], 0),
                      self.__step,
                      columns_heights[columns_heights.size - 1],
                      color=constants.plot_figure_color))

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

    def __get_elements_in_boundaries_probability(self, elements_in_boundaries_count: ndarray[float]) -> ndarray[float]:
        result: list[float] = []

        for element in elements_in_boundaries_count:
            result.append(element / self.data.sample_size)

        return np.array(result)

    @staticmethod
    def __configure_plot(axis, title: str, x_label: str, y_label: str) -> None:
        axis.set_title(title,
                       fontdict={'fontsize': constants.plot_title_font_size,
                                 'fontweight': 'bold', 'color': constants.plot_text_color})
        axis.set_xlabel(x_label,
                        fontdict={'fontsize': constants.plot_text_font_size, 'color': constants.plot_text_color})

        axis.set_ylabel(y_label,
                        fontdict={'fontsize': constants.plot_text_font_size, 'color': constants.plot_text_color})
