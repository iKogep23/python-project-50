#!/usr/bin/env python
import json
import yaml


def parse(data, format_):
    """Parses data"""
    if format_ == 'json':
        return json.loads(data)
    elif format_ == 'yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unsupported file format: {format_}")
