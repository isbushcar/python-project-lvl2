"""Generate diff between two json files."""

from gendiff.formaters.json_output import dump_json
from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish
from gendiff.parser import load_file_content

FORMATERS = {  # noqa: WPS407, WPS417
    'stylish': stylish,
    stylish: stylish,
    'plain': plain,
    plain: plain,
    'json': dump_json,
    dump_json: dump_json,
}


def generate_diff(first_file, second_file, formater=stylish):
    """Generate diff between two files."""
    first_file = load_file_content(first_file)
    second_file = load_file_content(second_file)
    formatted_output = FORMATERS[formater](find_diff(first_file, second_file))
    print(formatted_output)  # noqa: WPS421
    return formatted_output


def find_diff(first_file, second_file, level=0):  # noqa: WPS210
    """Find difference between data in two objects."""
    key_list = list(set(first_file.keys()).union(set(second_file.keys())))  # noqa: WPS221, E501
    key_list.sort()
    diff = {}
    for key in key_list:
        value_one = first_file.get(key)
        value_two = second_file.get(key)
        diff_template = {
            'added': value_two,
            'deleted': value_one,
            'unchanged': value_one,
            'changed': (value_one, value_two),
        }
        status = get_key_status(value_one, value_two)
        if status == 'nested':
            diff.setdefault((key, status), find_diff(value_one, value_two))
            continue
        diff.setdefault((key, status), diff_template[status])
    return diff


def get_key_status(value_one, value_two):
    """Return key status (added/deleted/changed/unchanged)."""
    if value_one is None:
        return 'added'
    if value_two is None:
        return 'deleted'
    if value_one == value_two:
        return 'unchanged'
    if isinstance(value_one, dict) and isinstance(value_two, dict):
        return 'nested'
    return 'changed'


def mark_unmarked_keys(element):  # TODO: delete
    """Check dict and mark unmarked keys as 'unchanged'."""
    if not isinstance(element, dict):
        return element
    updated_dict = {}
    for key, value in element.items():  # noqa: WPS110
        updated_dict.setdefault((key, 'unchanged'), mark_unmarked_keys(value))
    return updated_dict
