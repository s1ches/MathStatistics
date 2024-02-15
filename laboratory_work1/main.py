import data_reader.DataReader as DataReader
import data_handlers.DataHandler as DataHandler
from numpy import ndarray
from models.DataInfo import DataInfo
from constants import filepath, plot_style
from plot_builders.PlotBuilder import PlotBuilder


def main() -> None:
    data: ndarray[float] = DataReader.get_data(filepath)

    data_info: DataInfo = DataHandler.handle_data(data)
    print(data_info)

    plot_builder = PlotBuilder(data_info, plot_style)

    plot_builder.build()

if __name__ == '__main__':
    main()
