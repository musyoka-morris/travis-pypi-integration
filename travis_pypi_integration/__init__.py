from pymongoext import Model, DictField, IntField, Manipulator
from pymongo import MongoClient


__version__ = "2.1.1"


def add(a, b):
	"""A dummy function to add two variables"""
	return a + b


class YOBModel(Model):
	"""Dummy Mongo model"""
	@classmethod
	def db(cls):
		return MongoClient()['test_db']

	__schema__ = DictField(dict(
		yob=IntField(minimum=1900, maximum=2019, default=1990)
	))

	class AgeManipulator(Manipulator):
		def transform_outgoing(self, doc, model):
			doc['age'] = 2019 - doc['yob']
			return doc
