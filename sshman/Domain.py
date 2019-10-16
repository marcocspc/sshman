from .Errors import InvalidSSHConnectionAttribute, UserOrHostnameNotInformed
from .Colors import Color
import re

class SSHProfile:
    def __init__(self):
        self.profiles = []
    
    def __str__(self):
        string = ""
        cont = 1
        for sshprofile in self.profiles:
            string += str(cont) + " - " + sshprofile.name 
            string += "\n"
            cont += 1
        
        return string

class SSHConnection:
    def __init__(self, name, user, server_url, ssh_port = 22, key_path = None):
        self.name = name
        self.key_path = key_path
        self.user = user
        self.server_url = server_url
        self.ssh_port = ssh_port
        self.forwardings = []

    @classmethod
    def from_ssh_cmd(cls, ssh_cmd):
        #split everything
        ssh_cmd = ssh_cmd.split(' ')

        try:
            #search for user@host
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            at = [s for s in ssh_cmd if re.search(regex, s)]
            (user, host) = at[0].split('@')

            #TODO: continue this
        except ValueError:
            raise UserOrHostnameNotInformed("Please input username and host as user@host.")




    def get_ssh_command(self):
        if (self.name == None or self.user == None
             or self.server_url == None):
             raise InvalidSSHConnectionAttribute("SSHConnection's Name, User or Server URL not set")
        else:
            cmd = ["ssh", self.user + "@" + self.server_url]

            if (self.ssh_port != 22):
                cmd += ["-p" + str(self.ssh_port)]

            if (self.key_path != None):
                cmd += ["-i", self.key_path]
           
            for fwd in self.forwardings:
                cmd += ["-L", str(fwd.fwd_local_port) + ":" +
                        str(fwd.fwd_dest_ip_dns) + ":" +
                        str(fwd.fwd_dest_port)]
           
            return cmd

    def add_forwarding(fwd_local_port, fwd_dest_ip_dns, fwd_dest_port):
            forwarding = PortForwarding(fwd_local_port, 
                    fwd_dest_ip_dns, 
                    fwd_dest_port)
            self.forwardings.append(forwarding)

    def __str__(self):
        string = "--- Name: " + self.name + "\n"
        string += "User: " + self.user + "\n"
        string += "Server: " + self.server_url + "\n"
        string += "Port: " + str(self.ssh_port) + "\n"
        if self.key_path != None:
            string += "Key: " + str(self.key_path) + "\n"
        
        for fwd in self.forwardings: 
            string += ("Port forwarding: " + 
                        str(fwd.fwd_local_port) + ":" +
                        str(fwd.fwd_dest_ip_dns) + ":" +
                        str(fwd.fwd_dest_port) + "\n")
        
        return string

class PortForwarding:

    def __init__(self, local_port, dest_ip_dns, destination_port):
        self.fwd_local_port = local_port
        self.fwd_dest_ip_dns = dest_ip_dns
        self.fwd_dest_port = destination_port 
