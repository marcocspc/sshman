# -*- coding: utf-8 -*-

class InvalidSSHConnectionAttribute(Exception):
    """
        Raised when SSHConnection has one or
        more invalid attributes
    """
pass

class UserOrHostnameNotInformed(Exception):
    """
        Raised when user or hostname were not
        informed when trying to connect or add
        a new connection
    """
pass
