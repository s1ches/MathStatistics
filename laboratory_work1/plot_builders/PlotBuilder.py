from models.DataInfo import DataInfo
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from numpy import ndarray
import numpy as np
import constants
from scipy.stats import norm
from plot_builders.PlotBuilderHelper import PlotBuilderHelper


class PlotBuilder:
    def __init__(self, data: DataInfo, plot_style: str | None = None):
        self.data: DataInfo = data
        self.plot_style: str | None = plot_style
        self.__steps_count: int = data.sample_size // 10
        self.__step: float = data.spread / (self.__steps_count - 1)

        self.frequency_histogram_figure, self.frequency_histogram_axis = plt.subplots()
        self.probability_histogram_figure, self.probability_histogram_axis = plt.subplots()
        self.distribution_function_figure, self.distribution_function_axis = plt.subplots()
        self.distribution_polygon_figure, self.distribution_polygon_axis = plt.subplots()
        self.box_plot_figure, self.box_plot_axis = plt.subplots()

    def build(self) -> None:
        self.__build_frequency_histogram()
        self.probability_histogram_axis.plot()

        self.__build_probability_histogram()
        self.probability_histogram_axis.plot()

        self.__build_distribution_function()
        self.distribution_function_axis.plot()

        self.__build_distribution_polygon()
        self.distribution_polygon_axis.plot()

        self.__build_box_plot()
        self.box_plot_axis.plot()

        self.frequency_histogram_axis.legend(loc="upper left")
        self.probability_histogram_axis.legend(loc="upper left")
        self.distribution_function_axis.legend(loc="upper left")

        plt.show()

    def __build_frequency_histogram(self) -> None:
        boundaries: ndarray[float] = PlotBuilderHelper.get_boundaries(self.data, self.__step, self.__steps_count)

        elements_in_boundaries_count: ndarray[float] = PlotBuilderHelper.get_elements_count_in_boundaries(self.data,
                                                                                                          boundaries)

        self.__build_histogram(self.frequency_histogram_axis, boundaries, elements_in_boundaries_count)

        self.frequency_histogram_axis.plot()

        self.__build_data_info(self.frequency_histogram_axis, y_max=max(elements_in_boundaries_count) * 1.2)

        PlotBuilderHelper.configure_plot(self.frequency_histogram_axis, 'Частотная гистограмма', 'Данные', 'Частота')

    def __build_probability_histogram(self) -> None:
        boundaries: ndarray[float] = PlotBuilderHelper.get_boundaries(self.data, self.__step, self.__steps_count)

        elements_in_boundaries_count: ndarray[float] = PlotBuilderHelper.get_elements_count_in_boundaries(self.data,
                                                                                                          boundaries)

        elements_in_boundaries_probability: ndarray[float] = \
            PlotBuilderHelper.get_elements_in_boundaries_probability(self.data, elements_in_boundaries_count)

        elements_in_boundaries_heights = elements_in_boundaries_probability / self.__step

        self.__build_histogram(self.probability_histogram_axis, boundaries, elements_in_boundaries_heights)

        self.__build_normal_distribution(self.probability_histogram_axis)

        self.__build_data_info(self.probability_histogram_axis, y_max=max(elements_in_boundaries_heights) * 1.2)

        PlotBuilderHelper.configure_plot(self.probability_histogram_axis, 'Вероятностная гистограмма', 'X', 'Y')

    def __build_distribution_function(self) -> None:
        unic_elements: list[float] = list(set(self.data.variation_series))

        elements_counts: list[int] = list({i: self.data.variation_series.tolist().count(i)
                                           for i in self.data.variation_series}.values())

        elements_probability: list[float] = []

        for element in elements_counts:
            elements_probability.append(element / self.data.sample_size)

        probabilities_sums: list[float] = [sum(elements_probability[:i + 1]) for i in range(len(elements_probability))]

        probabilities_sums = [np.round(item, 4) for item in probabilities_sums]

        unic_elements = sorted(unic_elements)

        self.distribution_function_axis.plot([unic_elements[0] - self.__step, unic_elements[0]], [0, 0], color='blue')

        self.distribution_function_axis.plot([unic_elements[0], unic_elements[0]], [0, elements_probability[0]],
                                             color='blue')

        self.distribution_function_axis.plot(unic_elements, probabilities_sums, drawstyle='steps', color='blue')

        self.distribution_function_axis.plot([unic_elements[len(unic_elements) - 1], self.data.max_value + self.__step],
                                             [1, 1], color='blue')

        distribution_function_range = np.arange(self.data.min_value - self.__step, self.data.max_value + self.__step)
        self.distribution_function_axis.plot(distribution_function_range,
                                             norm.cdf(distribution_function_range,
                                                      self.data.mean, self.data.standard_deviation),
                                             color='red', label='Функция распределения')

        PlotBuilderHelper.configure_plot(self.distribution_function_axis, 'Функция распределения', 'Интервалы',
                                         'Вероятность попасть левее')

    def __build_distribution_polygon(self) -> None:
        self.distribution_polygon_axis.scatter(np.arange(0, self.data.sample_size), self.data.variation_series)

        PlotBuilderHelper.configure_plot(self.distribution_polygon_axis, 'Полигон распределения', 'Индексы', 'Данные')

    def __build_box_plot(self) -> None:
        self.box_plot_axis.boxplot(self.data.variation_series)

        PlotBuilderHelper.configure_plot(self.box_plot_axis, 'Box Plot', '', 'Данные')

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
