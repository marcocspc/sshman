# sshman
A simple ssh connection manager written in Python.

# Needed

- You need Python 3 installed on your system;
- You need OpenSSH client installed on your system. sshman will check for the existence of ssh binary.

# Installation

If you have system-wide permissions, use:
`pip3 install sshman`

If you want to install just for yourself (without administrative privileges), use:
`pip3 install sshman --user`

# Usage

## Add a new connection

To add a new connection, type:

`sshman add` or `sshman add <connection-name>`

You can replace 

Then press ENTER. sshman will prompt for needed info.

You can still use ssh syntax, like this:

`sshman add <connection-name> ssh user@host`

Or even: 

`sshman add <connection-name> ssh user@host -i /path/to/your/key`

Another way would be:

`sshman add <connection-name> ssh user@host -i /path/to/your/key -L port:remote-address:remote_port -L another:port:forwarding` 

If you want to use this mode, remember always to use \<connection-name\>.

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

### v0.3

- Add option to edit an existing connection; DONE
- Allow user to connect using a connection number. If no number or connection name is given, prompt; DONE
- Allow user to user to do the same as above with remove, show and edit; DONE
- List connections with a number on it's side, so the user knows which number to use when starting a connection; DONE
- Add connection number on 'show' command; DONE
- Add 'reorder' command, to reorder connections alphabetically; DONE
- Add option to insert a new connection using ssh syntax. Ex.: 'ssh user@host -i key_address -L localport1:remote_address1:remote_port1 -L localport2:remote_address2:remote_port2 -L etc"; DONE
- Allow user to quick input commands by their first letters. For example: 'sshman a' will be the same as 'sshan add', 'sshman c' will be the same as 'sshman connect', etc; DONE
- Update README.md to show how to install and include Python 3 as a requirement;
- Update README.md to match changes.
