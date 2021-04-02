#!usr/bin/env python3

"""Contains script that parses argument and calls generate_diff function."""


import argparse

from gendiff.generate_diff import generate_diff

parser = argparse.ArgumentParser(
    prog='generate diff', description='Generate diff',
)
parser.add_argument('-f', '--format', help='set format of output')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main():
    """Run generate_diff with parsed arguments."""
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
