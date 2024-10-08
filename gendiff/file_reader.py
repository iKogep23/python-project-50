#!/usr/bin/env python
import os


def read_file(filepath):
    """Reads data from a file"""
    with open(filepath, 'r') as file:
        return file.read()


def get_format(filepath):
    """Gets the file format"""
    root, ext = os.path.splitext(filepath)
    if ext == '.yaml' or ext == '.yml':
        return 'yaml'
    elif ext == '.json':
        return 'json'
    else:
        raise ValueError(f"Unsupported file format: {ext}")
