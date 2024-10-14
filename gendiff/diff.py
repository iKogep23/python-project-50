#!/usr/bin/env python
from gendiff.file_reader import read_file, get_format
from gendiff.parser import parse
from gendiff.data_comparer import compare_data
from gendiff.formatters.formatter import format_diff


def generate_diff(filepath1, filepath2, formatter="stylish"):
    format1 = get_format(filepath1)
    format2 = get_format(filepath2)
    data1 = parse(read_file(filepath1), format1)
    data2 = parse(read_file(filepath2), format2)
    diff = compare_data(data1, data2)
    return format_diff(diff, formatter)
