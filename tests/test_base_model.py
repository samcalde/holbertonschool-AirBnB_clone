#!/usr/bin/python3


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    b1 = BaseModel()
    b2 = BaseModel()
    b3 = BaseModel()

    def test_create(self):
        self.assertTrue(b1 != b2 != b3)
