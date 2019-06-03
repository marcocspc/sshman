# -*- coding: utf-8 -*-

from .Runner import Runner
import sys

def main():
    runner = Runner()
    try:
        if ('connect' in sys.argv and 
            sys.argv[sys.argv.index('connect') + 1] != None):
            name = sys.argv[sys.argv.index('connect') + 1]
            runner.connect(name)
        elif ('show' in sys.argv and 
            sys.argv[sys.argv.index('show') + 1] != None):
            name = sys.argv[sys.argv.index('show') + 1]
            runner.show_connection(name)
        elif 'add' in sys.argv:
            runner.add_prompt()
        elif ('remove' in sys.argv and 
            sys.argv[sys.argv.index('remove') + 1] != None):
            name = sys.argv[sys.argv.index('remove') + 1]
            runner.remove(name)
        elif 'list' in sys.argv:
            runner.list()
        elif 'help' in sys.argv:
            print_help()
        else:
            name = sys.argv[1]
            runner.connect(name)
    except (IndexError, AttributeError):
        print_help()
        raise
        

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
        "sshman remove <name>\n" +
        "Removes connection <name>.\n\n" +
        "sshman help\n" +
        "Prints this message.")
