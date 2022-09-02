#!/usr/bin/env python3
""" Module to define a custom shell to let a user
    work with the 'AirBnB' program interactively

"""

import cmd
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class definition for command interpretor """
    prompt = "(hbnb) "
    last_output = ""

    def emptyline(self):
        """ Handle response to empty line to the prompt """
        return False

    def do_shell(self, args):
        """ Run a shell command """
        print("Running shell command:", args)
        output = os.popen(args).read()
        print(output)
        self.last_output = output

    def do_echo(self, args):
        """ Print input or Replace $last with the last shell command """
        print(args.replace('$last', self.last_output))

    def do_quit(self, args):
        """ Quit command to exit the program\n """
        return True

    def do_EOF(self, args):
        """ EOF command to close the program\n """
        return True

    def do_create(self, args):
        """ Creates a new instance of 'BaseModel',
            saves it (to the JSON file) and prints the id
        """
        if args:
            create_list = list(args.split(" "))
            if create_list[0] == "BaseModel":
                b_object = BaseModel()
                b_object.save()
                print(b_object.id)
            else:
                print("** class doesn't exit **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        if args:
            my_list = list(args.split(" "))
            if len(my_list) == 2 and my_list[0] == "BaseModel" and\
                    storage._FileStorage__objects.get(my_list[1]):
                print(storage.all().get("{}.{}".format(BaseModel, my_list[1])))
            elif my_list[0] != "BaseModel":
                print("** class doesn't exit **")
            elif len(my_list) < 2:
                print("** instance id missing **")
            else:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        if args:
            my_list = list(args.split(" "))
            if len(my_list) == 2 and my_list[0] == "BaseModel" and\
                    storage._FileStorage__objects.get(my_list[1]):
                obj = storage.all().get("{}.{}".format(BaseModel, my_list[1]))
                del obj
                storage.save()
            elif my_list[0] != "BaseModel":
                print("** class doesn't exit **")
            elif len(my_list) < 2:
                print("** instance id missing **")
            else:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """ Prints all string representation of all instances
            based or not on the class name
        """
        if args:
            all_list = list(args.split(" "))
            if all_list[0] == "BaseModel":
                all_objs = list(storage.all().values())
                for obj in all_objs:
                    print(obj)
            else:
                print("** class doesn't exit **")
        else:
            print("** class name missing **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file
        """
        if args:
            update_list = list(args.split(" "))
            if len(update_list) == 4 and update_list[0] == "BaseModel" and\
                    storage._FileStorage__objects.get(update_list[1]):
                dict_obj = dict()
                index = 2
                dict_obj["id"] = str(update_list[1])
                while index <= len(update_list):
                    dict_obj[update_list[index]] = str(update_list[index + 1])
                    index += 2
                storage.new(dict_obj)
                storage.save()
            elif update_list[0] != "BaseModel":
                print("** class doesn't exit **")
            elif len(update_list) < 2:
                print("** instance id missing **")
            elif not storage._FileStorage__objects.get(update_list[1]):
                print("** no instance found **")
            elif len(update_list) < 3:
                print("** attribute name missing **")
            elif len(update_list) < 4:
                print("** value missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
