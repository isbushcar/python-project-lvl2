#!usr/bin/env python3

"""Contains script that parses argument and calls generate_diff function."""


import argparse

from gendiff_package.formaters.json_output import dump_json
from gendiff_package.formaters.plain import plain
from gendiff_package.formaters.stylish import stylish
from gendiff_package import generate_diff

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


FORMATERS = {  # noqa: WPS407, WPS417
    'stylish': stylish,
    stylish: stylish,
    'plain': plain,
    plain: plain,
    'json': dump_json,
    dump_json: dump_json,
}


def main():
    """Run generate_diff with parsed arguments."""
    generate_diff(args.first_file, args.second_file, FORMATERS[args.format])


if __name__ == '__main__':
    main()
