"""Generate diff between two json files."""

from gendiff import find_diff
from gendiff.formatters.json_output import dump_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import load_file_content

FORMATTERS = {  # noqa: WPS407, WPS417
    'stylish': stylish,
    'plain': plain,
    'json': dump_json,
}


def generate_diff(first_file, second_file, formatter='stylish'):
    """Generate diff between two files."""
    first_file = load_file_content(first_file)
    second_file = load_file_content(second_file)
    return FORMATTERS[formatter](find_diff(first_file, second_file))
