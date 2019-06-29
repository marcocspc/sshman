from .Errors import InvalidSSHConnectionAttribute
from .Colors import Color

class SSHProfile:
    def __init__(self):
        self.profiles = []
    
    def __str__(self):
        string = ""
        for sshprofile in self.profiles:
            string += sshprofile.name 
            string += "\n"
        
        return string

class SSHConnection:
    def __init__(self, name, user, 
        server_url, ssh_port = 22, key_path = None,
        fwd_local_port = None, fwd_dest_ip_dns = None, 
        fwd_dest_port = None):

        self.name = name
        self.key_path = key_path
        self.user = user
        self.server_url = server_url
        self.ssh_port = ssh_port
        self.forwardings = []

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
