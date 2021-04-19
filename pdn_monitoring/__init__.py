import datetime
import joblib
import pathlib
from typing import Union

import numpy as np
from scipy.fft import fft

PATH = pathlib.Path(__file__).parent


class PdnMonitor:
    """ This object is used to monitor assets in a power distribution network

    A random forest model is used as the classifier by default. The model can be changed with the
    load_model function.
    """
    def __init__(self):
        self.timestamp = datetime.datetime.utcnow().isoformat()
        self.standard_scaler = joblib.load(f'{PATH}/models/standard_scaler_2021_04_19.joblib')
        self.classification_model = joblib.load(f'{PATH}/models/random_forest_2021_04_19.joblib')

    def load_model(self, model_id: int = 1):
        """ Load a classification model (ordered from best to worst performing during modeling):
        1. Random forest
        2. Support vector
        3. Logistic regression
        4. Gradient boosting

        :param model_id: Model ID (see function description), defaults to 1
        """
        if not isinstance(model_id, int):
            raise TypeError('The model ID must be an integer.')
        elif model_id == 1:
            self.classification_model = joblib.load(f'{PATH}/models/random_forest_2021_04_19.joblib')
        elif model_id == 2:
            self.classification_model = joblib.load(f'{PATH}/models/support_vector_2021_04_19.joblib')
        elif model_id == 3:
            self.classification_model = joblib.load(f'{PATH}/models/logistic_regression_2021_04_19.joblib')
        elif model_id == 4:
            self.classification_model = joblib.load(f'{PATH}/models/gradient_boosting_2021_04_19.joblib')
        else:
            raise ValueError(f'The model ID {model_id} is not yet implemented.')

    @staticmethod
    def preprocess_data(data: Union[list, np.array]) -> np.array:
        """ Preprocess the data for the model

        :param data: Model input data
        :return: Preprocessed data
        """
        if len(data) != 1008:
            raise ValueError(f'The input data must contain 1008 elements, '
                             f'the given data contains {len(data)} elements.')

        try:
            voltage = [float(i) for i in data[:500]]
            current = [float(i) for i in data[500:1000]]
            sensor = float(data[1000])
        except ValueError:
            raise ValueError('The voltage, current and sensor data must be numerical.')

        voltage_ft = np.real(fft(voltage))[2:3]
        current_ft = np.real(fft(current))[1:3]

        array = np.append(voltage_ft, current_ft)
        array = np.append(array, sensor)

        return array

    def predict(self, input_data: list) -> int:
        """ Predict the state of the asset

        :param input_data: Input data used for predicting the state
        :return: Predicted state of the asset
        """
        data = self.preprocess_data(input_data).reshape(1, -1)
        model_input = self.standard_scaler.transform(data)
        return int(self.classification_model.predict(model_input)[0])
