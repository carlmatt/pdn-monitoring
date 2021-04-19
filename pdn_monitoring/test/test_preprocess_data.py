import pytest

import csv
import numpy as np
import pathlib
from pdn_monitoring import PdnMonitor

PATH = pathlib.Path(__file__).parent


def read_data(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data = row
    return data


def test_preprocess_data_1():
    test_data = read_data(f'{PATH}/test_data/test_case_1.csv')
    app = PdnMonitor()
    processed_data = app.preprocess_data(test_data)
    assert np.array_equal(processed_data.round(2), np.array([-11222.65, 16618.13, -2066.04, 31.74]))


def test_preprocess_data_2():
    test_data = read_data(f'{PATH}/test_data/test_case_2.csv')
    app = PdnMonitor()
    processed_data = app.preprocess_data(test_data)
    assert np.array_equal(processed_data.round(2), np.array([-3517.01, 11746.08, -267.25, 24.15]))


def test_preprocess_data_3():
    test_data = read_data(f'{PATH}/test_data/test_case_3.csv')
    app = PdnMonitor()
    processed_data = app.preprocess_data(test_data)
    assert np.array_equal(processed_data.round(2), np.array([433.87, 4710.45, 417.31, 22.71]))


def test_preprocess_data_value_error():
    test_data = [42, 'foo', 'bar']
    app = PdnMonitor()
    with pytest.raises(ValueError):
        app.preprocess_data(test_data)

