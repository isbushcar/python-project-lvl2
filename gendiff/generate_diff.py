"""Generate diff between two .json or .yaml files."""

from gendiff import find_diff
from gendiff.formatters.json_output import dump_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import load_file_content

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
FORMATTERS = {  # noqa: WPS407, WPS417
    STYLISH: stylish,
    PLAIN: plain,
    JSON: dump_json,
}


def generate_diff(first_file, second_file, formatter=STYLISH):
    """Generate diff between two files."""
    first_file = load_file_content(first_file, get_file_format(first_file))
    second_file = load_file_content(second_file, get_file_format(second_file))
    return FORMATTERS[formatter](find_diff(first_file, second_file))


def get_file_format(file_name):
    """Return file format."""
    format_index = file_name.rfind('.')
    return file_name[format_index + 1:]
