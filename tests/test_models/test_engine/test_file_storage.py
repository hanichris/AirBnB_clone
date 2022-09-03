#!/usr/bin/env python3
""" Unittest test cases for 'models.engine.file_storage' """
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage__init__(unittest.TestCase):
    """ Class to define test cases for public instance method '__init__()' """

    def test_output_type(self):
        self.assertIsNotNone(FileStorage())

    # Test cases for '__file_path' attribute
    def test__file_path_type(self):
        self.assertIsInstance(FileStorage()._FileStorage__file_path, str)

    def test__file_path_value(self):
        self.assertEqual(FileStorage()._FileStorage__file_path, 'file.json')

    # Test cases for '__objects' attribute
    def test__objects_type(self):
        self.assertIsInstance(FileStorage()._FileStorage__objects, dict)

    # Test cases for argument types
    def test_without_args(self):
        f1 = FileStorage()
        self.assertIsNotNone(f1)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage("id", "name")


class TestFileStorage_All(unittest.TestCase):
    """ Class to define test cases for public instance method 'all()' """

    def test_output_type(self):
        self.assertIsNotNone(FileStorage().all())
        self.assertIsInstance(FileStorage().all(), dict)

    def test_without_args(self):
        self.assertIsInstance(FileStorage().all(), dict)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage().all(1)


class TestFileStorage_New(unittest.TestCase):
    """ Class to define test cases for public instance method 'new(obj)' """

    def test_without_args(self):
        with self.assertRaises(TypeError):
            FileStorage().new()

    def test_with_args_str(self):
        with self.assertRaises(AttributeError):
            FileStorage().new("id")

    def test_with_args_positive_integer(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(1)

    def test_with_args_negative_integer(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(-1)

    def test_with_args_float(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(1.99999)

    def test_with_args_bool_true(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(True)

    def test_with_args_bool_false(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(False)

    def test_with_args_complex(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(complex(1))

    def test_with_args_invalid_dict(self):
        with self.assertRaises(AttributeError):
            FileStorage().new({"id": 1, "name": 2})

    def test_with_args_list(self):
        with self.assertRaises(AttributeError):
            FileStorage().new([12, 24, 36])

    def test_with_args_tuple(self):
        with self.assertRaises(AttributeError):
            FileStorage().new((12, 24, 36))

    def test_with_args_set(self):
        with self.assertRaises(AttributeError):
            FileStorage().new({'id', '__class__', 36})

    def test_with_args_frozenset(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(frozenset({'id', '__class__', 36}))

    def test_with_args_range(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(range(5))

    def test_with_args_bytes(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(b'id')

    def test_with_args_bytearray(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(bytearray(b'id'))

    def test_with_args_memoryview(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(memoryview(b'id'))

    def test_with_args_inf(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(float('Inf'))

    def test_with_args_negative_inf(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(float('-Inf'))

    def test_with_args_NaN(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(float('NaN'))

    def test_with_more_args(self):
        with self.assertRaises(TypeError):
            FileStorage().new("id", "__class__")


class TestFileStorage_Save(unittest.TestCase):
    """ Class to define test cases for public instance method 'save()' """

    def test_output_type(self):
        self.assertIsNone(FileStorage().save())

    def test_without_args(self):
        self.assertIsNone(FileStorage().save())

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage().save("id")


class TestFileStorage_Reload(unittest.TestCase):
    """ Class to define test cases for public instance method 'reload()' """

    def test_output_type(self):
        self.assertIsNone(FileStorage().reload())

    def test_without_args(self):
        self.assertIsNone(FileStorage().reload())

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage().reload("id")


if __name__ == '__main__':
    unittest.main()
