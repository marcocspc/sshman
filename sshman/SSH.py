# -*- coding: utf-8 -*-

from shutil import which
from subprocess import call

def is_ssh_installed():
    return which("ssh") is not None

def run(connection):
    if (is_ssh_installed):
        call(connection.get_ssh_command())
    else:
        print('SSH is not available.')