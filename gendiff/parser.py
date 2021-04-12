"""Parse file content."""


import json

import yaml


def load_file_content(file_name):
    """Return file's parsed content depending on its format."""
    formats_load = {
        'json': json.load,
        'yaml': yaml.safe_load,
    }
    file_format = get_format(file_name)
    file_content = formats_load[file_format](open(file_name))  # noqa: WPS515
    return parse(file_content, file_format)


def parse(file_content, file_format):
    """Parse file content depending on it's format."""
    converted = {}
    for key, value in file_content.items():  # noqa: WPS110
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
