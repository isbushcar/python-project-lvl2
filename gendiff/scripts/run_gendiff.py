#!usr/bin/env python3

"""Contains script that parses argument and calls generate_diff function."""


import argparse

from gendiff.formatter import stylish
from gendiff.generate_diff import generate_diff

parser = argparse.ArgumentParser(
    prog='generate diff', description='Generate diff',
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f',
    '--format',
    help='set format of output',
    default=stylish,
)
args = parser.parse_args()


def main():
    """Run generate_diff with parsed arguments."""
    generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
