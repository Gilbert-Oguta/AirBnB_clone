#!/usr/bin/python3
"""
Entry point module for Console program
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """The Console Program"""
    prompt = "(hbnb) "

    def do_quit(self, _):
        """Quit command to exit the program

        Usage: quit
        """
        sys.exit()

    def do_EOF(self, _):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        return False

    def do_create(self, line):
        """Create a new instance of data models, save it (to the JSON file)
        and print the id

        Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
            return
        arg = line.split()[0]
        try:
            if arg == "BaseModel":
                new = BaseModel()
            elif arg == "User":
                new = User()
            elif arg == "State":
                new = State()
            elif arg == "City":
                new = City()
            elif arg == "Amenity":
                new = Amenity()
            elif arg == "Place":
                new = Place()
            elif arg == "Review":
                new = Review()
            new.save()
            print(new.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id

        Usage: show <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(args[0], args[1])
                print(storage.all()[key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(args[0], args[1])
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name

        Usage: all <class name> or all
        """
        args = line.split()
        if line and args[0] not in ["BaseModel", "User", "State", "City",
                                    "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            print([str(v) for v in storage.all().values()])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all()[key]
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(obj, args[2], args[3])
                    storage.save()
            except KeyError:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
