#!/usr/bin/python3


"""
This module will  be used to test the BaseModel class
"""


from models.base_model import BaseModel


base1 = BaseModel()
print(base1.id)
print("--")
print(base1.created_at)
print("--")
print(base1)
print("--")
print("to_dict test:")
for key, value in base1.to_dict().items():
    print(f"{key} = {value}")