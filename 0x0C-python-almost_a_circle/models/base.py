#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        args:
        list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
        list_oobjs: A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string
        Args:
        json_string: A string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
        **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jf:
                list_dicts = Base.from_json_string(jf.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
