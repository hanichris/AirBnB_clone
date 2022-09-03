#!/usr/bin/env python3
""" Module to define a custom shell to let a user
    work with the 'AirBnB' program interactively

"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class definition for command interpretor """
    prompt = "(hbnb) "

    def emptyline(self):
        """ Handle response to empty line to the prompt """
        return False

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """ EOF command to close the program """
        return True

    def do_create(self, args):
        """ Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if args:
            create_list = list(args.split(" "))
            if create_list[0] == "BaseModel":
                b_object = BaseModel()
                b_object.save()
                print(b_object.id)
            elif create_list[0] == "User":
                b_object = User()
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
            if len(my_list) == 2:
                if my_list[0] == "BaseModel" and\
                        storage.all().get("{}.{}".format("BaseModel",
                                          str(my_list[1]))):
                    obj = storage.all().get("{}.{}".format("BaseModel",
                                            str(my_list[1])))
                elif my_list[0] == "User" and\
                        storage.all().get("{}.{}".format("User",
                                          str(my_list[1]))):
                    obj = storage.all().get("{}.{}".format("User",
                                            str(my_list[1])))
                print(obj)
            elif my_list[0] != "BaseModel" or my_list[0] != "User":
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
            if len(my_list) == 2:
                if my_list[0] == "BaseModel" and\
                        storage.all().get("{}.{}".format("BaseModel",
                                          str(my_list[1]))):
                    obj = storage.all().get("{}.{}".format("BaseModel",
                                            str(my_list[1])))
                elif my_list[0] == "User" and\
                        storage.all().get("{}.{}".format("User",
                                          str(my_list[1]))):
                    obj = storage.all().get("{}.{}".format("User",
                                            str(my_list[1])))
                del obj
                storage.save()
            elif my_list[0] != "BaseModel" or my_list[0] != "User":
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
                all_objs = list(storage.all().items())
                for k, v in all_objs:
                    if k.startswith("BaseModel"):
                        print(v)
            elif all_list[0] == "User":
                all_objs = list(storage.all().items())
                for k, v in all_objs:
                    if k.startswith("User"):
                        print(v)
            else:
                print("** class doesn't exit **")
        else:
            all_objs = list(storage.all().values())
            for obj in all_objs:
                print(obj)

    def do_update(self, args):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file
        """
        if args:
            update_list = list(args.split(" "))
            if len(update_list) == 4:
                if update_list[0] == "BaseModel" and\
                        storage.all().get("{}.{}".format("BaseModel",
                                          str(update_list[1]))):
                    obj = storage.all().get("{}.{}".format("BaseModel",
                                            str(update_list[1])))
                elif update_list[0] == "User" and\
                        storage.all().get("{}.{}".format("User",
                                          str(update_list[1]))):
                    obj = storage.all().get("{}.{}".format("User",
                                            str(update_list[1])))
                index = 2
                while index < len(update_list):
                    if update_list[index] != "id" or\
                            update_list[index] != "created_at" or\
                            update_list[index] != "updated_at":
                        obj.__dict__[update_list[index]] = update_list[index+1]
                        index += 2
                storage.new(obj)
                storage.save()
            elif update_list[0] != "BaseModel" or update_list[0] != "User":
                print("** class doesn't exit **")
            elif len(update_list) < 2:
                print("** instance id missing **")
            elif not storage.all().get("{}.{}".format("BaseModel",
                                       update_list[1])) or\
                    not storage.all().get("{}.{}".format("User",
                                          update_list[1])):
                print("** no instance found **")
            elif len(update_list) < 3:
                print("** attribute name missing **")
            elif len(update_list) < 4:
                print("** value missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
