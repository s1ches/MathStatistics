import data_reader.DataReader as DataReader
from constants import filepath
from data_handlers import DataHandler
from models.DataModel import DataModel
from plot_builders.PlotBuilder import build_plot


def main() -> None:
    data: DataModel = DataReader.get_data(filepath)

    data = DataHandler.handle_data(data)

    print(data)
    build_plot(data)


if __name__ == '__main__':
    main()
