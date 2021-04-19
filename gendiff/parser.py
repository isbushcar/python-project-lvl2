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
    return formats_load[file_format](open(file_name))  # noqa: WPS515


def get_format(file_name):
    """Return string with file's format."""
    formats = {
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml',
    }
    return formats[file_name[file_name.rfind('.'):]]
