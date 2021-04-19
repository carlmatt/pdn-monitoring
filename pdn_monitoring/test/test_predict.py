import pytest

import csv
import pathlib
from pdn_monitoring import PdnMonitor

PATH = pathlib.Path(__file__).parent


def read_data(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data = row
    return data


def test_predict_rf_1():
    test_data = read_data(f'{PATH}/test_data/test_case_1.csv')
    app = PdnMonitor()
    prediction = app.predict(test_data)
    assert prediction == 3


def test_predict_rf_2():
    test_data = read_data(f'{PATH}/test_data/test_case_2.csv')
    app = PdnMonitor()
    prediction = app.predict(test_data)
    assert prediction == 3


def test_predict_rf_3():
    test_data = read_data(f'{PATH}/test_data/test_case_3.csv')
    app = PdnMonitor()
    prediction = app.predict(test_data)
    assert prediction == 1


def test_predict_sv_1():
    test_data = read_data(f'{PATH}/test_data/test_case_1.csv')
    app = PdnMonitor()
    app.load_model(model_id=2)
    prediction = app.predict(test_data)
    assert prediction == 1


def test_predict_sv_2():
    test_data = read_data(f'{PATH}/test_data/test_case_2.csv')
    app = PdnMonitor()
    app.load_model(model_id=2)
    prediction = app.predict(test_data)
    assert prediction == 3


def test_predict_sv_3():
    test_data = read_data(f'{PATH}/test_data/test_case_3.csv')
    app = PdnMonitor()
    app.load_model(model_id=2)
    prediction = app.predict(test_data)
    assert prediction == 1


def test_predict_lr_1():
    test_data = read_data(f'{PATH}/test_data/test_case_1.csv')
    app = PdnMonitor()
    app.load_model(model_id=3)
    prediction = app.predict(test_data)
    assert prediction == 3


def test_predict_lr_2():
    test_data = read_data(f'{PATH}/test_data/test_case_2.csv')
    app = PdnMonitor()
    app.load_model(model_id=3)
    prediction = app.predict(test_data)
    assert prediction == 3


def test_predict_lr_3():
    test_data = read_data(f'{PATH}/test_data/test_case_3.csv')
    app = PdnMonitor()
    app.load_model(model_id=3)
    prediction = app.predict(test_data)
    assert prediction == 3


def test_predict_gb_1():
    test_data = read_data(f'{PATH}/test_data/test_case_1.csv')
    app = PdnMonitor()
    app.load_model(model_id=4)
    prediction = app.predict(test_data)
    assert prediction == 2


def test_predict_gb_2():
    test_data = read_data(f'{PATH}/test_data/test_case_2.csv')
    app = PdnMonitor()
    app.load_model(model_id=4)
    prediction = app.predict(test_data)
    assert prediction == 3


def test_predict_gb_3():
    test_data = read_data(f'{PATH}/test_data/test_case_3.csv')
    app = PdnMonitor()
    app.load_model(model_id=4)
    prediction = app.predict(test_data)
    assert prediction == 1
