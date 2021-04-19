import pytest

from pdn_monitoring import PdnMonitor
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.ensemble._gb import GradientBoostingClassifier
from sklearn.linear_model._logistic import LogisticRegression
from sklearn.svm._classes import SVC


def test_load_model_1():
    app = PdnMonitor()
    app.load_model(model_id=1)
    assert type(app.classification_model) is RandomForestClassifier


def test_load_model_2():
    app = PdnMonitor()
    app.load_model(model_id=2)
    assert type(app.classification_model) is SVC


def test_load_model_3():
    app = PdnMonitor()
    app.load_model(model_id=3)
    assert type(app.classification_model) is LogisticRegression


def test_load_model_4():
    app = PdnMonitor()
    app.load_model(model_id=4)
    assert type(app.classification_model) is GradientBoostingClassifier


def test_load_model_type_error():
    app = PdnMonitor()
    with pytest.raises(TypeError):
        app.load_model(model_id='foo')


def test_load_model_value_error():
    app = PdnMonitor()
    with pytest.raises(ValueError):
        app.load_model(model_id=42)
