import data_reader.DataReader as DataReader
import data_handlers.DataHandler as DataHandler
from numpy import ndarray
from models.DataInfo import DataInfo
from constants import *


def main() -> None:
    data: ndarray[float] = DataReader.get_data(filepath)

    data_info: DataInfo = DataHandler.handle_data(data)
    print(data_info)




if __name__ == '__main__':
    main()
