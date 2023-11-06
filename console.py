#!/usr/bin/python3


"""
This module contains the command interpreter for the AirBnB console
"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    allowed_classes = ('BaseModel', 'User')

    def do_destroy(self, arg):
        """
        removes an instance from the database
        """
        args = arg.split()
        if args:
            class_name = args[0]
            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return
            try:
                instance_id = args[1]
            except:
                print("** instance id missing **")
                return
            all_instances = storage.all()
            if all_instances:
                try:
                    del all_instances[f'{class_name}.{instance_id}']
                    storage.save()
                except:
                    print("** no instance found **")
            else:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints all instances saves of a single class or every class
        """
        if arg in self.allowed_classes or arg == '': #update to print only the class
            instances_dictionary = storage.all()
            for key, value in instances_dictionary.items():
                class_and_id = key.split(".")
                instance_class = class_and_id[0]
                if arg == '' or instance_class == arg:
                    print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates the value of an attribute
        """
        args = arg.split()
        if args:
            class_name = args[0]
            try:
                instance_id = args[1]
            except:
                print("** instance id missing **")
                return
            try:
                attribute_name = args[2]
            except:
                print("** attribute name missing **")
                return
            try:
                attribute_value = args[3]
            except:
                print("** value missing **")
                return
        else:
            print("** class name missing **")
            return

        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        
        all_instances = storage.all()
        if all_instances:
            try:
                instance = all_instances[f'{class_name}.{instance_id}']
            except:
                print("** no instance found **")
                return

        if getattr(instance, attribute_name, False):
            attribute_type = type(getattr(instance, attribute_name))
            attribute_value = attribute_type(attribute_value)
        else:
            attribute_value = attribute_value.strip('"')
        setattr(instance, attribute_name, attribute_value)

    def do_show(self, arg):
        """
        shows an instance based on class name and id
        """
        args = arg.split()
        if args:
            class_name = args[0]
            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return
            try:
                instance_id = args[1]
            except:
                print("** instance id missing **")
                return
            all_instances = storage.all()
            if all_instances:
                try:
                    instance = all_instances[f'{class_name}.{instance_id}']
                    print(instance)
                except:
                    print("** no instance found **")
            else:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        """
        if arg:
            if arg in self.allowed_classes:
                new_model = arg()
                new_model.save()
                print (new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_help(self, args):
        """
        Help command
        """
        super().do_help(args)

    def do_quit(self, arg):
        """
        Quit command. Ends interpreter
        """
        return True

    def do_EOF(self,arg):
        """
        EOF command. Ends interpreter
        """
        return True
    
    def emptyline(self):
        """
        Does nothing
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
