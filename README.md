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

## Adding a new connection

To add a new connection, type:

`sshman add` or `sshman add <connection-name>`

Then press ENTER. sshman will prompt for needed info.

You can still use ssh syntax, like this:

`sshman add <connection-name> ssh user@host`

Or even: 

`sshman add <connection-name> ssh user@host -i /path/to/your/key`

Another way would be:

`sshman add <connection-name> ssh user@host -i /path/to/your/key -L port:remote-address:remote_port -L another:port:forwarding` 

If you want to use this mode, remember always to use \<connection-name\>.

You can also replace `add` for just `a` on all commands above, for example:

`sshman a <connection-name>`
`sshman a`

This is a quicker way to do stuff.

## Connecting to existing connection

Both ways will work:

`sshman connect <connection-name>` or `sshman <connection-name>`

Where \<connection-name\> is, well, the connection name.

Like on 'add' command, you can replace `connect` for just `c`.

`sshman c`

## List all available connections

`sshman list` or `sshman l`

## Show detailed information about specific connection

`sshman show <connection-name>` or `sshman s`

## Remove connection

`sshman remove <connection-name>` or `sshman rm <connection-name>`

## Help

`sshman help` or `sshman h`

Or even just:

`sshman`

## TODO

### v0.4

- [ ] Add support for SCP via upload and download commands;
- [ ] Add option to print ssh command to given connection;
- [ ] Update help command;
- [ ] Update README.md to match changes; 
- [ ] Allow user to check if host is up using command "check", and to keep watching using -w.

### v0.3 

- [x] Add option to edit an existing connection; 
- [x] Allow user to connect using a connection number. If no number or connection name is given, prompt; 
- [x] Allow user to user to do the same as above with remove, show and edit; 
- [x] List connections with a number on it's side, so the user knows which number to use when starting a connection; 
- [x] Add connection number on 'show' command; 
- [x] Add 'reorder' command, to reorder connections alphabetically; 
- [x] Add option to insert a new connection using ssh syntax. Ex.: 'ssh user@host -i key_address -L localport1:remote_address1:remote_port1 -L localport2:remote_address2:remote_port2 -L etc"; 
- [x] Allow user to quick input commands by their first letters. For example: 'sshman a' will be the same as 'sshan add', 'sshman c' will be the same as 'sshman connect', etc; 
- [x] Update README.md to show how to install and include Python 3 as a requirement; 
- [x] Update README.md to match changes. 
