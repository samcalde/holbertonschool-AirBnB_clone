#!/usr/bin/python3


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    base1 = BaseModel()
    base2 = BaseModel()
    base3 = BaseModel()

    def test_create(self):
        self.assertTrue(base1.id != base2.id)

if (__name__ == '__main__'):
    unittest.main()
