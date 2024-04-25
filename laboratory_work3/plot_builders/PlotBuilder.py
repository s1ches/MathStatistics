from constants import y_prediction
from data_handlers.DataHandler import get_prediction
from models.DataModel import DataModel
import matplotlib.pyplot as plt


def build_plot(data: DataModel):
    figure, axes = plt.subplots()

    axes.scatter(data.x_sample, data.y_sample, color='green', label="Sample Data")

    axes.plot(get_prediction(data.x_mean, data.regression_coefficient, data.y_sample, data.y_mean),
              data.y_sample,
              label="Regression Line")

    axes.plot([min(data.x_sample), data.x_prediction], [y_prediction, y_prediction], linestyle="--", color="red")
    axes.plot([data.x_prediction, data.x_prediction], [min(data.y_sample), y_prediction], linestyle="--", color="red")
    axes.scatter(data.x_prediction, y_prediction, color="red", linewidths=5, label=f"Prediction with y={y_prediction}")

    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_title('Linear Regression')
    axes.grid(True)

    plt.legend(loc="best")
    plt.show()

