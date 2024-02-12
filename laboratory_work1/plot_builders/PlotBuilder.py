from models.DataInfo import DataInfo
import matplotlib.pyplot as plt
from numpy import ndarray


class PlotBuilder:
    def __init__(self, data: DataInfo, plot_style: str | None = None):
        self.data: DataInfo = data
        self.plot_style: str | None = plot_style
        self.steps_count: int = data.sample_size // 10
        self.step: int = int(data.spread / (self.steps_count - 1))

    def build_frequency_histogram(self) -> None:
        return None

    def build_probability_histogram(self) -> None:
        return None

    def build_distribution_function(self) -> None:
        return None

    def build_box_plot(self) -> None:
        return None

    def _get_borders(self) -> enumerate[float]:
        return None
