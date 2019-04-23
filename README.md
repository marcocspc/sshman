# sshman
A simple ssh connection manager written in Python.

# Needed

You need OpenSSH client installed on your system. sshman will check for the existence of ssh binary.

# Usage

## Add a new connection

To add a new connection, type:

`sshman add`

Then press ENTER. sshman will prompt for connection name, user, password and other needed information.

## Connect to existing connection

Both ways will work:

`sshman connect <connection-name>` or `sshman <connection-name>`

Where \<connection-nam\> is, well, the connection name.

## List all available connections

`sshman list`

## Show detailed information about specific connection

`sshman show <connection-name>`

Where \<connection-name\> is, well, the connection name.

## Remove connection

`sshman remove <connection-name>` 

Where \<connection-name\>... I believe that, at this point, I don't need to tell you what that means. :P

## Help

`sshman help`

Or just:

`sshman`

Will print a quick help text.
