import data_reader.DataReader as DataReader
from numpy import ndarray
from constants import data_for_lower_confidence_limit_for_variance_filepath
import data_handlers.DataHandler as DataHandler


def main() -> None:
    data: ndarray[float] = DataReader.get_data(data_for_lower_confidence_limit_for_variance_filepath)

    print(f'Нижняя доверительная граница: {DataHandler.get_lower_confidence_limit_for_variance(data)}')


if __name__ == '__main__':
    main()
