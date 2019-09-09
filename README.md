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

Where \<connection-name\>...

## Remove connection

`sshman remove <connection-name>` 

## Help

`sshman help`

Or just:

`sshman`

Will print a quick help text.

## TODO

- Add option to edit an existing connection;
- Allow user to connect using a connection number. If no number or connection name is given, prompt;
- List connections with a number on it's side, so the user knows which number to use when starting a connection;
- Add connection number on 'show' command;
- Add 'reorder' command, to reorder connections alphabetically;
- Add option to insert a new connection using ssh syntax. Ex.: 'ssh user@host -i key_address -L localport1:remote_address1:remote_port1 -L localport2:remote_address2:remote_port2 -L etc".
