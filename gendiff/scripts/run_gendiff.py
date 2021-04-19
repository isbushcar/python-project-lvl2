#!usr/bin/env python3

"""Contains script that parses argument and calls generate_diff function."""


import argparse

from gendiff import generate_diff
from gendiff.formaters.json_output import dump_json
from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish

parser = argparse.ArgumentParser(
    prog='generate diff', description='Generate diff',
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f',
    '--format',
    help='set format of output',
    default='stylish',
)
args = parser.parse_args()


FORMATTERS = {  # noqa: WPS407
    'stylish': stylish,
    'plain': plain,
    'json': dump_json,
}


def main():
    """Run generate_diff with parsed arguments."""
    print(generate_diff(args.first_file, args.second_file, FORMATTERS[args.format]))  # noqa: WPS421, E501


if __name__ == '__main__':
    main()
