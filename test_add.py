from travis_pypi_integration import add
from pymongoext import Model, DictField, IntField, Manipulator
from pymongo import MongoClient
from datetime import datetime


class TestModel(Model):
    @classmethod
    def db(cls):
        return MongoClient()['test_db']

    __schema__ = DictField(dict(
        yob=IntField(minimum=1900, maximum=2019, default=1990)
    ))

    __indexes__ = ['yob']

    class AgeManipulator(Manipulator):
        def transform_outgoing(self, doc, model):
            doc['age'] = datetime.utcnow().year - doc['yob']
            return doc


def test_answer():
    assert add(1, 2) == 3


def test_pymongoext():
    assert TestModel.insert_one({'yob': 1991}) is not None
    assert TestModel.find().count() == 1
    assert TestModel.find_one().age == 28
