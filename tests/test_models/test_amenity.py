#!/usr/bin/python3
""" Unittest test cases for 'models.base_model' """
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_Instantiation(unittest.TestCase):
    """Test the instantiation of the Amenity class."""

    def setUp(self):
        self.model = Amenity()

    def tearDown(self):
        del self.model

    def test_instance_exists(self):
        self.assertIsNotNone(self.model)

    def test_class_attributes(self):
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_class_attributes_type(self):
        self.assertIsInstance(getattr(Amenity, 'name'), str)

    def test_assigned_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_unique_ids(self):
        my_model = Amenity()
        self.assertNotEqual(self.model.id, my_model.id)

    def test_creation_time(self):
        my_model = Amenity()
        self.assertNotEqual(self.model.created_at, my_model.created_at)

    def test_no_args_instantiation(self):
        self.assertIsInstance(self.model, Amenity)

    def test_args_instantiation(self):
        my_model = Amenity("name", "number")
        self.assertIsInstance(my_model, Amenity)

    def test_no_kwargs_instantiation(self):
        self.assertIsInstance(self.model, Amenity)

    def test_kwargs_instantiation(self):
        my_model = Amenity(name="My First Model", number=89)
        self.assertIsInstance(self.model, Amenity)

    def test_created_at_type(self):
        self.assertTrue(isinstance(self.model.created_at, datetime))

    def test_updated_at_type(self):
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_id_type(self):
        self.assertTrue(isinstance(self.model.id, str))


class TestAmenity__str__(unittest.TestCase):
    """ Class to define test cases for public instance method '__str__()' """

    def setUp(self):
        self.model = Amenity()

    def tearDown(self):
        del self.model

    def test_output_type(self):
        self.assertIsNotNone(self.model.__str__())
        self.assertIsInstance(self.model.__str__(), str)

    def test_contains_class_name(self):
        self.assertTrue(
                self.model.__str__().__contains__(
                    self.model.__class__.__name__
                    )
                )

    def test_contains_id(self):
        self.assertTrue(
                self.model.__str__().__contains__(self.model.id)
                )

    def test_contains__dict__(self):
        self.assertTrue(self.model.__str__().__contains__("id"))
        self.assertTrue(self.model.__str__().__contains__("created_at"))
        self.assertTrue(self.model.__str__().__contains__("updated_at"))

    def test_without_args(self):
        self.assertIsInstance(self.__str__(), str)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.model.__str__("id")


class TestAmenity_Save(unittest.TestCase):
    """ Class to define test cases for public instance method 'save()' """

    def setUp(self):
        self.model = Amenity()

    def tearDown(self):
        del self.model

    def test_output_type(self):
        self.assertIsNone(self.model.save())

    def test_updated_at_type(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_update_time(self):
        updated_time = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, updated_time)

    def test_without_args(self):
        self.assertIsNone(self.model.save())

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.model.save("id")


class TestAmenity_to_dict(unittest.TestCase):
    """Test the `to_dict` instance method of the Amenity class."""

    def setUp(self):
        self.model = Amenity()

    def tearDown(self):
        del self.model

    def test_output_contents(self):
        model_json = self.model.to_dict()
        self.assertDictEqual(model_json,
                             {
                                'id': self.model.id,
                                'created_at': self.model.created_at.strftime(
                                                '%Y-%m-%dT%H:%M:%S.%f'),
                                'updated_at': self.model.updated_at.strftime(
                                                '%Y-%m-%dT%H:%M:%S.%f'),
                                '__class__': Amenity.__name__
                             })

    def test_output_type(self):
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_date_format(self):
        model_json = self.model.to_dict()
        self.assertIsInstance(model_json['created_at'], str)
        self.assertIsInstance(model_json['updated_at'], str)

    def test_others_type(self):
        model_json = self.model.to_dict()
        self.assertIsInstance(model_json['id'], str)
        self.assertIsInstance(model_json['__class__'], str)

    def test_without_args(self):
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.model.to_dict("id")


if __name__ == '__main__':
    unittest.main()
