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
            elif create_list[0] == "State":
                b_object = State()
                b_object.save()
                print(b_object.id)
            elif create_list[0] == "City":
                b_object = City()
                b_object.save()
                print(b_object.id)
            elif create_list[0] == "Amenity":
                b_object = Amenity()
                b_object.save()
                print(b_object.id)
            elif create_list[0] == "Place":
                b_object = Place()
                b_object.save()
                print(b_object.id)
            elif create_list[0] == "Review":
                b_object = Review()
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
        all_variables = list(["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"])
        if args:
            my_list = list(args.split(" "))
            if len(my_list) == 2 and my_list[0] in all_variables:
                if my_list[0] == "BaseModel" and\
                        storage.all().get(f"{'BaseModel'}.{str(my_list[1])}")\
                            is not None:
                    obj = storage.all().get(f"{'BaseModel'}.{str(my_list[1])}")
                elif my_list[0] == "User" and\
                        storage.all().get(f"{'User'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'User'}.{str(my_list[1])}")
                elif my_list[0] == "State" and\
                        storage.all().get(f"{'State'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'State'}.{str(my_list[1])}")
                elif my_list[0] == "City" and\
                        storage.all().get(f"{'City'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'City'}.{str(my_list[1])}")
                elif my_list[0] == "Amenity" and\
                        storage.all().get(f"{'Amenity'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Amenity'}.{str(my_list[1])}")
                elif my_list[0] == "Place" and\
                        storage.all().get(f"{'Place'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Place'}.{str(my_list[1])}")
                elif my_list[0] == "Review" and\
                        storage.all().get(f"{'Review'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Review'}.{str(my_list[1])}")
                print(obj)
            elif my_list[0] not in all_variables:
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
        all_variables = list(["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"])
        if args:
            my_list = list(args.split(" "))
            if len(my_list) == 2 and my_list[0] in all_variables:
                if my_list[0] == "BaseModel" and\
                        storage.all().get(f"{'BaseModel'}.{str(my_list[1])}")\
                            is not None:
                    obj = storage.all().get(f"{'BaseModel'}.{str(my_list[1])}")
                elif my_list[0] == "User" and\
                        storage.all().get(f"{'User'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'User'}.{str(my_list[1])}")
                elif my_list[0] == "State" and\
                        storage.all().get(f"{'State'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'State'}.{str(my_list[1])}")
                elif my_list[0] == "City" and\
                        storage.all().get(f"{'City'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'City'}.{str(my_list[1])}")
                elif my_list[0] == "Amenity" and\
                        storage.all().get(f"{'Amenity'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Amenity'}.{str(my_list[1])}")
                elif my_list[0] == "Place" and\
                        storage.all().get(f"{'Place'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Place'}.{str(my_list[1])}")
                elif my_list[0] == "Review" and\
                        storage.all().get(f"{'Review'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Review'}.{str(my_list[1])}")
                del obj
                storage.save()
            elif my_list[0] not in all_variables:
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
            elif all_list[0] == "State":
                all_objs = list(storage.all().items())
                for k, v in all_objs:
                    if k.startswith("State"):
                        print(v)
            elif all_list[0] == "City":
                all_objs = list(storage.all().items())
                for k, v in all_objs:
                    if k.startswith("City"):
                        print(v)
            elif all_list[0] == "Amenity":
                all_objs = list(storage.all().items())
                for k, v in all_objs:
                    if k.startswith("Amenity"):
                        print(v)
            elif all_list[0] == "Place":
                all_objs = list(storage.all().items())
                for k, v in all_objs:
                    if k.startswith("Place"):
                        print(v)
            elif all_list[0] == "Review":
                all_objs = list(storage.all().items())
                for k, v in all_objs:
                    if k.startswith("Review"):
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
        all_variables = list(["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"])
        if args:
            my_list = list(args.split(" "))
            if len(my_list) == 4 and my_list[0] in all_variables:
                if my_list[0] == "BaseModel" and\
                        storage.all().get(f"{'BaseModel'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'BaseModel'}.{str(my_list[1])}")
                elif my_list[0] == "User" and\
                        storage.all().get(f"{'User'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'User'}.{str(my_list[1])}")
                elif my_list[0] == "State" and\
                        storage.all().get(f"{'State'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'State'}.{str(my_list[1])}")
                elif my_list[0] == "City" and\
                        storage.all().get(f"{'City'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'City'}.{str(my_list[1])}")
                elif my_list[0] == "Amenity" and\
                        storage.all().get(f"{'Amenity'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Amenity'}.{str(my_list[1])}")
                elif my_list[0] == "Place" and\
                        storage.all().get(f"{'Place'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Place'}.{str(my_list[1])}")
                elif my_list[0] == "Review" and\
                        storage.all().get(f"{'Review'}.{str(my_list[1])}") \
                            is not None:
                    obj = storage.all().get(f"{'Review'}.{str(my_list[1])}")

                index = 2
                while index < len(my_list):
                    if my_list[index] != "id" or\
                            my_list[index] != "created_at" or\
                            my_list[index] != "updated_at":
                        obj.__dict__[my_list[index]] = my_list[index+1]
                        index += 2
                storage.new(obj)
                storage.save()
            elif my_list[0] not in all_variables:
                print("** class doesn't exit **")
            elif len(my_list) < 2:
                print("** instance id missing **")
            elif not storage.all().get(f"{'BaseModel'}.{my_list[1]}") or\
                    not storage.all().get(f"{'User'}.{my_list[1]}") or\
                    not storage.all().get(f"{'State'}.{my_list[1]}") or\
                    not storage.all().get(f"{'City'}.{my_list[1]}") or\
                    not storage.all().get(f"{'Amenity'}.{my_list[1]}") or\
                    not storage.all().get(f"{'Place'}.{my_list[1]}") or\
                    not storage.all().get(f"{'Review'}.{my_list[1]}"):
                print("** no instance found **")
            elif len(my_list) < 3:
                print("** attribute name missing **")
            elif len(my_list) < 4:
                print("** value missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
