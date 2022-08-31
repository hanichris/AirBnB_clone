#  AirBnB clone - The console

The project implementation is by use of [cmd](https://docs.python.org/3.10/library/cmd.html) and other python3 modules to wrap together a command line interpretor as a framework for testing and protoyping the AirBnB inteface from the command line.

### Description
The command line interpretor is essentially made up of several python modules which allow interactive and non-interactive execution including file storage etc.

### Interactive Execution Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Execution Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Examples
**coming soon**

## Testing
    python3 -m unittest discover tests


© ALX SOFTWARE ENGINEERING 2022