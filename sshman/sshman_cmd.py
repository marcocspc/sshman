# -*- coding: utf-8 -*-

from .Runner import Runner
from .Errors import SSHConnectionNotFoundError, SSHConnectionNameNotInformed
import sys

def main():
    runner = Runner()

    #if structure to allow user to call commands using initials
    #For example: c will connect, rm will remove, etc
    if 'c' in sys.argv:
        sys.argv[sys.argv.index('c')] = 'connect'
    elif 'e' in sys.argv:
        sys.argv[sys.argv.index('e')] = 'edit'
    elif 's' in sys.argv:
        sys.argv[sys.argv.index('s')] = 'show'
    elif 'a' in sys.argv:
        sys.argv[sys.argv.index('a')] = 'add'
    elif 'rm' in sys.argv:
        sys.argv[sys.argv.index('rm')] = 'remove'
    elif 'ro' in sys.argv:
        sys.argv[sys.argv.index('ro')] = 'reorder'
    elif 'h' in sys.argv:
        sys.argv[sys.argv.index('h')] = 'help'
    elif 'l' in sys.argv:
        sys.argv[sys.argv.index('l')] = 'list'


    try:
        if 'connect' in sys.argv:
            try:
                name_or_number = sys.argv[sys.argv.index('connect') + 1]
                runner.connect(name_or_number)
            except IndexError:
                runner.connect_prompt()
        elif 'show' in sys.argv:
            try:
                name_or_number = sys.argv[sys.argv.index('show') + 1]
                runner.show_connection(name_or_number)
            except IndexError:
                runner.show_prompt()
        elif 'add' in sys.argv:
            try:
                pos = sys.argv.index('add') + 1
                if 'ssh' in sys.argv[pos:]:
                    if sys.argv.index('ssh') == pos:
                        raise SSHConnectionNameNotInformed("Please input a connection name to use this mode.")
                    elif sys.argv.index('ssh') == pos + 1:
                        runner.add_cmd(sys.argv[pos], sys.argv[pos + 1:])
                else:
                    runner.add_prompt(sys.argv[pos])
            except IndexError:
                runner.add_prompt()
        elif 'edit' in sys.argv:
            try:
                name_or_number = sys.argv[sys.argv.index('edit') + 1]
                runner.edit_prompt(name_or_number)
            except IndexError:
                runner.edit_prompt()
        elif ('remove' in sys.argv and 
            sys.argv[sys.argv.index('remove') + 1] != None):
            name = sys.argv[sys.argv.index('remove') + 1]
            runner.remove(name)
        elif 'list' in sys.argv:
            runner.list()
        elif 'reorder' in sys.argv:
            runner.reorder()
        elif 'help' in sys.argv:
            print_help()
        else:
            name = sys.argv[1]
            runner.connect(name)
    except (IndexError, AttributeError):
        print_help()
    except SSHConnectionNotFoundError as e:
        print(e)
        

def print_help():
    print("Usage:\n\n" + 
        "sshman connect <name>\n" +
        "Connects to connection <name>.\n\n" +
        "sshman show <name>\n" +
        "Show details about connection <name>.\n\n" +
        "sshman list\n" +
        "Lists all connections available.\n\n" +
        "sshman add\n" +
        "Will prompt data for a new connection.\n\n" +
        "sshman edit <name>\n" +
        "Will prompt to update connection <name> parameters.\n\n"
        "sshman remove <name>\n" +
        "Removes connection <name>.\n\n" +
        "sshman help\n" +
        "Prints this message.")
