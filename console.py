#!/usr/bin/python3
""" Module to define a custom shell to let a user
    work with the 'AirBnB' program interactively

"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """ Class definition for command interpretor """
    prompt = "(hbnb) "
    __valid_classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            ]

    def emptyline(self):
        """ Handle response to empty line to the prompt."""
        return False

    def do_quit(self, args):
        """ Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """ EOF command to close the program."""
        return True

    def do_create(self, args):
        """ Creates a new instance of a model.

        The created instance is saved to the JSON file
        and id of the model is printed out to the console.
        """
        if args:
            args_list = shlex.split(args)
            if args_list[0] in HBNBCommand.__valid_classes:
                new_object = eval(args_list[0])()
                new_object.save()
                print(new_object.id)
            else:
                print("** class doesn't exit **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """ Prints the string representation of an instance.

        The representation is based on the class name and id.
        """
        if args:
            args_list = shlex.split(args)
            if args_list[0] not in HBNBCommand.__valid_classes:
                print("** class doesn't exist **")
                return
            elif len(args_list) == 1:
                print("** instance id missing **")
                return
            key = f"{args_list[0]}.{args_list[1]}"
            if key in storage.all():
                print(f"{storage.all()[key]}")
            else:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id.
            
        The changes made are saved in the JSON file.
        """
        if args:
            args_list = shlex.split(args)
            if args_list[0] not in HBNBCommand.__valid_classes:
                print("** class doesn't exist **")
                return
            elif len(args_list) == 1:
                print("** instance id missing **")
                return
            key = f"{args_list[0]}.{args_list[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """ Prints all string representations of all instances.

        The format used to print the instances is either
        `all <class name>` or `all`. If the former is used, only
        instances of that class are printed out. Otherwise, all the
        instances regardless of class are printed out.
        """
        list_objects = []
        if args:
            args_list = shlex.split(args)
            if args_list[0] not in HBNBCommand.__valid_classes:
                print("** class doesn't exist **")
                return
            all_objects = storage.all()
            for key, value in all_objects.items():
                key_list = key.split(".")
                if key_list[0] == args_list[0]:
                    list_objects.append(f"{value}")
            print(list_objects)
        else:
            all_objects = storage.all()
            for value in all_objects.values():
                list_objects.append(f"{value}")
            print(list_objects)

    def do_update(self, args):
        """ Updates an instance based on the class name and id.

        Format:
        update <class name> <id> <attr name> "<atrr value>".
        """
        if args:
            args_list = shlex.split(args)
            if args_list[0] not in HBNBCommand.__valid_classes:
                print("** class doesn't exist **")
                return
            elif len(args_list) == 1:
                print("** instance id missing **")
                return
            key = f"{args_list[0]}.{args_list[1]}"
            if key not in storage.all():
                print("** no instance found **")
                return
            elif len(args_list) == 2:
                print("** attribute name missing **")
                return
            elif len(args_list) == 3:
                print("** value missing **")
                return
            elif len(args_list) == 4:
                attr_name = args_list[2]
                attr_value = args_list[3]
                try:
                    setattr(storage.all()[key], attr_name, attr_value)
                except AttributeError:
                    print("** attribute name missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
