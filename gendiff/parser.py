"""Parse file content."""


import json

import yaml


def get_file_content(file_name):
    """Return file's content depending on its format."""
    formats_load = {
        'json': json.load,
        'yaml': yaml.safe_load,
    }
    return formats_load[get_format(file_name)](open(file_name))  # noqa: WPS515


def parse(file_or_its_content, file_format=''):
    """Parse file content depending on it's format."""
    if not file_format:
        file_format = get_format(file_or_its_content)
    if not isinstance(file_or_its_content, dict):
        file_or_its_content = get_file_content(file_or_its_content)
    converted = {}
    for key, value in file_or_its_content.items():  # noqa: WPS110
        if isinstance(value, dict):
            converted.setdefault(
                str(get_encoded(key, file_format)),
                parse(value, file_format),
            )
        else:
            converted.setdefault(
                get_encoded(key, file_format),
                get_encoded(value, file_format),
            )
    return converted


def get_format(file_name):
    """Return string with file's format."""
    formats = {
        '.json': 'json',
        '.yaml': 'yaml',
    }
    return formats[file_name[file_name.rfind('.'):]]


def get_encoded(element, file_format):
    """Return string with encoded item depending on format."""
    if isinstance(element, str):
        return element
    formats_dump = {
        'json': json.dumps,
        'yaml': yaml.dump,
    }
    convert = formats_dump[file_format]
    return convert(element).rstrip().rstrip('...').rstrip().strip('"')
