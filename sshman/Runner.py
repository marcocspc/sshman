# -*- coding: utf-8 -*-

from .Dumper import SSHProfileDumper
from . import SSH as ssh 
from .Domain import SSHConnection
from .Domain import SSHProfile
from .Domain import PortForwarding 

class Runner:
    def __init__(self):
        self.dumper = SSHProfileDumper()
        self.ssh_profile = self.dumper.load()
    
    def connect(self, connection_name):
        if self.ssh_profile == None:
            print("There are no SSH Connections set.")
        else:
            ssh_connection = None
            for connection in self.ssh_profile.profiles:
                if connection.name == connection_name:
                    ssh_connection = connection 
                    break
            
            ssh.run(ssh_connection)
    
    def show_connection(self, connection_name):
        if self.ssh_profile == None:
            print("There are no SSH Connections set.")
        else:
            for connection in self.ssh_profile.profiles:
                if connection.name == connection_name:
                    print(connection)
                    break
        
    def list(self):
        if self.ssh_profile == None:
            print("There are no SSH Connections set.")
        else:
            print(self.ssh_profile, end="")

    def add(self, name, fwd_list, key_path, user, 
        server_url, ssh_port):

        new_ssh = SSHConnection(name, user, server_url, ssh_port, key_path)

        for fwd in fwd_list:
            new_ssh.forwardings.append(fwd)
        
        self.ssh_profile.profiles.append(new_ssh)
        self.dumper.save(self.ssh_profile)

        
    
    def add_prompt(self):
        if self.ssh_profile == None:
            self.ssh_profile = SSHProfile()

        name = get_string_input("Insert connection name:", "new_connection")

        user = input("Insert username: ")
        if user == None or user == "":
            print("Cannot proceed without a username.")
            return

        server_url = input("Insert Server URL: ")
        if server_url == None or user == "":
            print("Cannot proceed without Server URL.")
            return
        
        ssh_port = 22
        option = get_string_input("Will you change the default SSH port? [y/n]", "n")
        if str.lower(option) == "y":
            ssh_port = get_int_input("Insert SSH port: ", 22)

        ssh_key = None
        option = get_string_input("Will you use ssh private key? [y/n]", "n")
        if str.lower(option) == "y":
            ssh_key = input("Insert SSH key path: ")
        
        local_port, dest_ip_dns, dest_port = None, None, None
        option = get_string_input("Will you use port forwarding? [y/n]", "n")
        forwardings = []

        while(str.lower(option) == "y"):
            local_port = input("Insert local port: ")
            dest_ip_dns = input("Insert destination URL: ")
            dest_port = input("Insert destination port: ") 

            fwd = PortForwarding(local_port, dest_ip_dns,
                    dest_port)
            forwardings.append(fwd)

            option = get_string_input("Will you add another port forwarding? [y/n]", "n")

        self.add(name, forwardings, ssh_key, user, 
            server_url, ssh_port)

    def remove(self, connection_name):
        if self.ssh_profile == None:
            print("There are no SSH Connections set.")
        else:
            for connection in self.ssh_profile.profiles:
                if connection.name == connection_name:
                    self.ssh_profile.profiles.remove(connection)
                    self.dumper.save(self.ssh_profile)
                    break

#aux functions
def get_int_input (message, default_value):
    try:
        return int(input(message + " [Default " + str(default_value) + "] "))
    except ValueError:
        return default_value

def get_string_input (message, default_value):
    try:
        string = str(input(message + " [Default " + str(default_value) + "] "))
        return string if string != "" else default_value
    except ValueError:
        return default_value
