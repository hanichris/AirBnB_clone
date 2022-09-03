#!/usr/bin/python3
"""FileStorage class that performs serialization/deserialization.

The class serializes instances to a JSON file and deserializes
the JSON file to instances.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage(object):
    """ Class definition for storage of JSON data into file

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): object storage structure

    """
    __file_path = os.path.relpath('file.json')
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Insert `obj` into the class attribute `__objects`.

        The key used in the dictionary `__objects` is the id of
        the object. The format is `<class name>.id` eg BaseModel.123

        Args:
            obj (object): instance of a class.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes '__objects' into the JSON file '__file_path' """
        objects_json = {
                key: value.to_dict()
                for key, value in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(objects_json, f)

    def reload(self):
        """ Deserializes the JSON file '__file_path' into '__objects' """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                objects = json.load(f)
        except FileNotFoundError:
            pass
        else:
            for obj in objects.values():
                cls_name = obj['__class__']
                del obj['__class__']
                self.new(eval(f"{cls_name}")(**obj))
