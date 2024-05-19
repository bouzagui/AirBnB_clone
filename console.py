#!/usr/bin/python3
"""the console 'main' part of the project"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "
    classes = [
        "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    do_EOF = do_quit

    def do_create(self, line):
        """Creates a new instance of a given class, saves it
        (to the JSON file) and prints the id."""
        if line == '':
            print('** class name missing **')
        elif line not in self.classes:
            print('** class doesn\'t exist **')
        else:
            if line == "BaseModel":
                obj = BaseModel()
                storage.save()
            elif line == "User":
                obj = User()
                storage.save()
            elif line == "State":
                obj = State()
                storage.save()
            elif line == "City":
                obj = City()
                storage.save()
            elif line == "Amenity":
                obj = Amenity()
                storage.save()
            elif line == "Place":
                obj = Place()
                storage.save()
            elif line == "Review":
                obj = Review()
                storage.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, line):
        """deletes the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print('** no instance found **')
            else:
                del storage.all()[key]
                storage.save()
    

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name."""
        args = line.split()
        if len(args) == 0:
            for obj in storage.all().values():
                print(obj)
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)

    def do_update(self, line):
        """Updates the instance based on the
        class name and id."""
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print('** no instance found **')
            elif len(args) == 2:
                print('** attribute name missing **')
            elif len(args) == 3:
                print('** value missing **')
            else:
                setattr(obj, args[2], args[3])
                storage.save()

if __name__ == '__main__':
    """main function"""
    HBNBCommand().cmdloop()
