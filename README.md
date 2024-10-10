### Hexlet tests and linter status:
[![Actions Status](https://github.com/iKogep23/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/iKogep23/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/97d4cbb0ee75dbc0acf2/maintainability)](https://codeclimate.com/github/iKogep23/python-project-50/maintainability)
[![Python CI](https://github.com/iKogep23/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/iKogep23/python-project-50/actions/workflows/pyci.yml)

### Difference calculator
___
Gendiff is a command line utility for calcule differencies between two configuration files.
The tool analyzes the files and displays the differences in a human-readable format.
It supports JSON, YAML and YML file formats.
The result can be presented in the following formats: stylish, json and plain.

### Dependencies
___
This package requires the following dependencies:

    - python, version 3.11 and up
    - pyyaml, version 6.0.2 and up 

To install them run make install command.

### Installation
___
    - Run make package-install to install this package. Run make build to build the project.

### Installation to a virtual environment
___
If your system refuses to install the package, one way out is to install this package in a virtual environment.

    - Run python3 -m venv environment_name to build a python venv. Make virtual environment outside of the project.
    - Run environment_name/bin/pip3 install python-project-50/dist/*.whl to install this package to a virtual environment you just created.

### Help output
___
To display help on using the utility, you need to run it with the -h parameter:
```
gendiff -h
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file            Path to json or yml file
  second_file           Path to second file in same format

options:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output: stylish, plain or json

gendiff created by Bessonov Igor
```

### Examples of use:
___
Recording an example of comparing two simple json files stylish format:
[![asciicast](https://asciinema.org/a/4HtEexWL25M1NnNP8vH4K6PPx.svg)](https://asciinema.org/a/4HtEexWL25M1NnNP8vH4K6PPx)

Recording an example of comparing two simple yaml files stylish format:
[![asciicast](https://asciinema.org/a/w0OBblPKDW1n1tbCr236vA3fi.svg)](https://asciinema.org/a/w0OBblPKDW1n1tbCr236vA3fi)

Recording an example of comparing two nested json files stylish format:
[![asciicast](https://asciinema.org/a/GJySB1OdDZ1ET3LmL5EtS7dN9.svg)](https://asciinema.org/a/GJySB1OdDZ1ET3LmL5EtS7dN9)

Recording an example of comparing two nested json files in plain format:
[![asciicast](https://asciinema.org/a/L4dFPH8WyuxQ1U7Ja1F9TU1fz.svg)](https://asciinema.org/a/L4dFPH8WyuxQ1U7Ja1F9TU1fz)

Recording an example of comparing two nested json files in json format:
[![asciicast](https://asciinema.org/a/yU2zsIVDNUr8jRxfcuw8c4nJC.svg)](https://asciinema.org/a/yU2zsIVDNUr8jRxfcuw8c4nJC)
