"""Parse file content."""


import json

import yaml


def load_file_content(file_name, file_format):
    """Return file's parsed content depending on its format."""
    formats_load = {
        'json': json.load,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load,
    }
    return formats_load[file_format](open(file_name))  # noqa: WPS515
