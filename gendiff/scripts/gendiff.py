#!/usr/bin/env python
import argparse


from gendiff.gendiff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
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
