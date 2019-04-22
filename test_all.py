from travis_pypi_integration import *


def test_answer():
    assert add(1, 2) == 3


def test_pymongoext():
    assert YOBModel.insert_one({'yob': 1991}) is not None
    assert YOBModel.find_one().age == 28
