# Project Overview

This project contains multiple Python programs along with their corresponding unit tests.
All test cases using the Arrange-Act-Assert (AAA) methodology.

## Setting Up the Environment

### 1. Create a Virtual Environment
Using a virtual environment (`venv`) helps isolate dependencies for the project.

#### On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```sh
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
Ensure you have all required packages installed:
```sh
pip install -r requirements.txt
```

## Running Tests

To run the tests, execute:

### Run All Tests with `unittest`
```sh
python -m unittest discover -s tests
```

### Run All Tests with `pytest`
```sh
pytest tests/
```

### Run a Specific Test File
```sh
pytest tests/test_hackerrank_funny_string.py
```

### Run a Single Test Case
```sh
pytest tests/test_hackerrank_funny_string.py::TestFunnyString::test_funny_string
```

### Run All Tests Using a Single Script
If you have a script to run all tests from the `tests/` directory:
```sh
cd tests
python run_all_tests.py
```

## Updating Dependencies
If new dependencies are added, update `requirements.txt` with:
```sh
pip freeze > requirements.txt
```

## Deactivating the Virtual Environment
When done, deactivate the virtual environment:
```sh
deactivate
```

