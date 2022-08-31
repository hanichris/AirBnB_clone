#!/usr/bin/env Python3
""" File storage module """

import os
import json


class FileStorage(object):
    """ Class definition for storage of JSON data into file

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): object storage structure

    """

    def __init__(self):
        """ The constructor to initialize new file storage instances """
        try:
            self.__file_path = os.path.relpath('file.json')
        except FileNotFoundError:
            pass
        self.__objects = dict()

    def all(self):
        """ Returns the dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ Adds a new object in dictionary '__objects' """
        if isinstance(obj, dict)\
                and isinstance(obj.get('__class__'), str)\
                and isinstance(obj.get('id'), str):
            self.__objects.update({"{}.{}".format(obj.get('__class__'),
                                                  obj.get('id')): obj})
        else:
            self.__objects.update({"{}.{}".format(obj.__class__.__name__,
                                                  obj.id): obj.to_dict()})

    def save(self):
        """ Serializes '__objects' into the JSON file '__file_path' """
        with open(self.__file_path, mode="a", encoding="UTF8") as f:
            for item in self.__objects:
                json.dump(item, f)

    def reload(self):
        """ Deserializes the JSON file '__file_path' into '__objects' """
        d = dict()
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                self.__objects.update(json.load(f))
        except FileNotFoundError:
            pass
