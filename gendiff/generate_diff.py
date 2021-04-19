"""Generate diff between two json files."""

from gendiff.formaters.json_output import dump_json
from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish
from gendiff.parser import load_file_content

FORMATTERS = {  # noqa: WPS407, WPS417
    'stylish': stylish,
    'plain': plain,
    'json': dump_json,
}


def generate_diff(first_file, second_file, formatter=stylish):
    """Generate diff between two files."""
    first_file = load_file_content(first_file)
    second_file = load_file_content(second_file)
    if isinstance(formatter, str):
        formatter = FORMATTERS[formatter]
    formatted_output = formatter(find_diff(first_file, second_file))
    print(formatted_output)  # noqa: WPS421
    return formatted_output


def find_diff(first_file, second_file):  # noqa: WPS210
    """Find difference between data in two objects."""
    key_list = list(first_file.keys() | second_file.keys())
    key_list.sort()
    diff = {}
    for key in key_list:
        value_one = first_file.get(key, '[do not exist]')
        value_two = second_file.get(key, '[do not exist]')
        if isinstance(value_one, dict) and isinstance(value_two, dict):
            diff[(key, 'nested')] = find_diff(value_one, value_two)
        else:
            status, keys_value = get_key_status_and_value(value_one, value_two)
            diff[key, status] = keys_value
    return diff


def get_key_status_and_value(value_one, value_two):
    """Return key status (added/deleted/changed/unchanged)."""
    if value_one == '[do not exist]':
        return 'added', value_two
    if value_two == '[do not exist]':
        return 'deleted', value_one
    if value_one == value_two:
        return 'unchanged', value_one
    return 'changed', (value_one, value_two)
