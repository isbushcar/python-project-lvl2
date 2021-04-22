"""Generate diff between two json files."""

from uuid import uuid1

from gendiff.formatters.json_output import dump_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import load_file_content

FORMATTERS = {  # noqa: WPS407, WPS417
    'stylish': stylish,
    'plain': plain,
    'json': dump_json,
}

UUID = uuid1()


def generate_diff(first_file, second_file, formatter='stylish'):
    """Generate diff between two files."""
    first_file = load_file_content(first_file)
    second_file = load_file_content(second_file)
    return FORMATTERS[formatter](find_diff(first_file, second_file))


def find_diff(first_file, second_file):  # noqa: WPS210
    """Find difference between data in two objects."""
    key_list = list(first_file.keys() | second_file.keys())
    key_list.sort()
    diff = {}
    for key in key_list:
        value_one = first_file.get(key, UUID)
        value_two = second_file.get(key, UUID)
        if isinstance(value_one, dict) and isinstance(value_two, dict):
            diff[key] = {
                'status': 'nested',
                'value': find_diff(value_one, value_two),
            }
        else:
            status, keys_value = get_key_status_and_value(value_one, value_two)
            diff[key] = {'status': status, 'value': keys_value}
    return diff


def get_key_status_and_value(value_one, value_two):
    """Return key status (added/deleted/changed/unchanged)."""
    if value_one == UUID:
        return 'added', value_two
    if value_two == UUID:
        return 'deleted', value_one
    if value_one == value_two:
        return 'unchanged', value_one
    return 'changed', {'old value': value_one, 'new value': value_two}
