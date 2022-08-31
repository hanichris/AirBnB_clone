#!/usr/bin/env python3
""" Unittest test cases for 'models.base_model' """

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase__init__(unittest.TestCase):
    """ Class to define test cases for public instance method '__init__()' """

    @classmethod
    def setUp(self):
        b = BaseModel()
        self.id = b.id
        self.created_at = b.created_at
        self.updated_at = b.updated_at
        self.__str__ = b.__str__
        self.save = b.save
        self.to_dict = b.to_dict
        print("SetUp Class")

    def test_output_type(self):
        self.assertIsNotNone(BaseModel())

    # Test cases for 'id' attribute
    def test_id_type(self):
        self.assertIsInstance(self.id, str)

    def test_id_is_unique(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    # Test cases for 'created_at' attribute
    def test_created_at_type(self):
        self.assertIsInstance(self.created_at, datetime)

    def test_creation_time(self):
        b1 = BaseModel()
        self.assertGreater(b1.created_at, self.created_at)

    # Test cases for 'updated_at' attribute
    def test_updated_at_type(self):
        self.assertIsInstance(self.updated_at, datetime)

    def test_update_time(self):
        self.assertNotEqual(self.created_at, self.updated_at)

    # Test cases for argument types
    def test_without_args(self):
        b1 = BaseModel()
        self.assertIsNotNone(b1)

    def test_with_args(self):
        b1 = BaseModel("id", "name")
        self.assertIsNotNone(b1)

    def test_without_kwargs(self):
        b1 = BaseModel()
        self.assertIsNotNone(b1)

    def test_with_kwargs(self):
        b1 = BaseModel({"id": 11})
        self.assertIsNotNone(b1)


class TestBase__str__(unittest.TestCase):
    """ Class to define test cases for public instance method '__str__()' """

    @classmethod
    def setUp(self):
        b = BaseModel()
        self.id = b.id
        self.created_at = b.created_at
        self.updated_at = b.updated_at
        self.__str__ = b.__str__
        self.save = b.save
        self.to_dict = b.to_dict
        print("SetUp Class")

    def test_output_type(self):
        self.assertIsNotNone(self.__str__())
        self.assertIsInstance(self.__str__(), str)

    def test_contains_class_name(self):
        b1 = BaseModel()
        self.assertTrue(b1.__str__().__contains__(b1.__class__.__name__))

    def test_contains_id(self):
        b1 = BaseModel()
        self.assertTrue(b1.__str__().__contains__(b1.id))

    def test_contains__dict__(self):
        b1 = BaseModel()
        self.assertTrue(b1.__str__().__contains__("id"))
        self.assertTrue(b1.__str__().__contains__("created_at"))
        self.assertTrue(b1.__str__().__contains__("updated_at"))

    def test_without_args(self):
        self.assertIsInstance(self.__str__(), str)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.__str__("id")


class TestBase_Save(unittest.TestCase):
    """ Class to define test cases for public instance method 'save()' """

    @classmethod
    def setUp(self):
        b = BaseModel()
        self.id = b.id
        self.created_at = b.created_at
        self.updated_at = b.updated_at
        self.__str__ = b.__str__
        self.save = b.save
        self.to_dict = b.to_dict
        print("SetUp Class")

    def test_output_type(self):
        self.assertIsNone(self.save())

    def test_updated_at_type(self):
        self.assertIsInstance(self.updated_at, datetime)

    def test_update_time(self):
        b1 = BaseModel()
        b1.save()
        self.assertGreater(b1.updated_at, b1.created_at)

    def test_without_args(self):
        self.assertIsNone(self.save())

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.save("id")


class TestBase_To_Dict(unittest.TestCase):
    """ Class to define test cases for public instance method 'to_dict()' """

    @classmethod
    def setUp(self):
        b = BaseModel()
        self.id = b.id
        self.created_at = b.created_at
        self.updated_at = b.updated_at
        self.__str__ = b.__str__
        self.save = b.save
        self.to_dict = b.to_dict
        print("SetUp Class")

    def test_output_type(self):
        self.assertIsInstance(self.to_dict(), dict)

    def test_without_args(self):
        self.assertIsInstance(self.to_dict(), dict)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.to_dict("id")


if __name__ == '__main__':
    unittest.main()
