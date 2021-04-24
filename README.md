# pdn-monitoring
Model for monitoring assets in a power distribution network

## Requirements

This project requires Python 3.7 or later. The project uses [Poetry](https://python-poetry.org/) for dependency
management. Installation instructions for Poetry can be found [here](https://python-poetry.org/docs/#installation).
Poetry can also be installed using pip with

```shell
pip install --user poetry
```

The dependencies can be installed with

```shell
poetry install
```

The development dependencies are required for running the unit tests and the cells in the Jupyter notebooks. However,
the tool itsel can be used without the development dependencies. To install only the main dependencies, run

```shell
poetry install --no-dev
```

## Running the unit tests

### Using Docker

Requires GNU Make and Docker. To run the unit tests using Docker, simply run

```shell
make run-test
```

### Locally

Before running the unit tests locally, please ensure that your machine meets the requirements mentioned in the _Requirements_ section. The unit tests can be run
with

```shell
poetry run pytest
```

## Using the tool

The easiest way to use this tool is to navigate to the root directory of this project and start your Python shell

```shell
python3
```

Then, in your Python shell, import the module and create an instance of the PdnMonitor. To get more details about
the tool, you can use the `help` function.

```python
from pdn_monitoring import PdnMonitor
monitor = PdnMonitor()
help(monitor)
```

To easily try out the tool, load some test data and make a prediction.

```python
import csv
with open('pdn_monitoring/test/test_data/test_case_1.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        test_data = row

monitor.predict(test_data)
```

If you use your own data, the data should match the training data but should not include a label. It should consist of
the following (in the correct order):

1. One full 50 Hz cycle (500 samples) of the voltage measured on the asset
2. One full 50 Hz cycle (500 samples) of the current measured on the asset
3. Six readings taken from the six additional sensors
4. Timestamp of recording
5. ID of the device that captured the recording

The tool uses a random forest classifier model by default. You can change the model using the `load_model` function. The
supported models are

| ID | Model                  |
|---:|:-----------------------|
| 1  | Random forest          |
| 2  | Support vector machine |
| 3  | Logistic regression    |
| 4  | Gradient boosting      |

```python
monitor.load_model(2)
```

## Updating the dependencies

The dependencies can be updated to the lastest versions with

```shell
poetry update
```
