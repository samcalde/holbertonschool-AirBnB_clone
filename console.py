#!/usr/bin/python3


"""
This module contains the command interpreter for the AirBnB console
"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

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
