#!/usr/bin/env python
import argparse
# from gendiff.diff import generate_diff
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


def get_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        epilog='gendiff created by Bessonov Igor'
    )
    parser.add_argument("first_file",
                        help='Path to json or yml file')
    parser.add_argument("second_file",
                        help='Path to second file in same format')
    parser.add_argument("-f", "--format", default="stylish",
                        choices=["stylish", "plain", "json"],
                        help='set format of output: stylish, plain or json')
    args = parser.parse_args()
    return args


def main():
    """Run generate_diff."""
    args = get_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
