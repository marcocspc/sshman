# -*- coding: utf-8 -*-

import os
from shutil import which
from subprocess import call 

def is_ssh_installed():
    return which("ssh") is not None

def run(connection):
    if (is_ssh_installed):
        cmd = connection.get_ssh_command()
        call(cmd)
    else:
        print('SSH is not available.')
