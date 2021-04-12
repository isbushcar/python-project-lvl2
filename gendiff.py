"""Generate diff between two json files."""

from functools import partial

from gendiff_package.formaters.stylish import stylish
from gendiff_package.parser import load_file_content


def generate_diff(first_file, second_file, formater=stylish):
    """Generate diff between two files."""
    first_file = load_file_content(first_file)
    second_file = load_file_content(second_file)
    formatted_output = formater(find_diff(first_file, second_file))
    print(formatted_output)  # noqa: WPS421
    return formatted_output


def find_diff(first_file, second_file, level=0):  # noqa: WPS210
    """Find difference between data in two objects."""
    key_list = mark_keys(first_file, second_file)
    diff = {}
    for element in key_list:
        key, status = element
        value_one = first_file.get(key)
        value_two = second_file.get(key)
        diff_template = {
            'added': mark_unmarked_keys(value_two),
            'deleted': mark_unmarked_keys(value_one),
            'unchanged': mark_unmarked_keys(value_one),
            'changed': (mark_unmarked_keys(value_one), mark_unmarked_keys(
                value_two,
            )),
        }
        if isinstance(value_one, dict) and isinstance(value_two, dict):
            dict_diff = find_diff(value_one, second_file.get(key), level + 1)
            diff.setdefault(element, dict_diff)
            continue
        diff.setdefault(element, diff_template[status])
    return diff


def mark_keys(items_one, items_two):
    """Return sorted list with tuple (key, mark)."""
    get_status = partial(get_key_status, items_one, items_two)
    marked_keys = []
    keys = set(items_one.keys()).union(set(items_two.keys()))
    for key in keys:
        marked_keys.append((key, get_status(key)))
    marked_keys.sort(key=lambda marked_key: marked_key[0])
    return marked_keys


def get_key_status(items_one, items_two, key):
    """Return key status ((added/deleted/changed/unchanged)."""
    keys_one = set(items_one.keys())
    keys_two = set(items_two.keys())
    if key in keys_two.difference(keys_one):
        return 'added'
    if key in keys_one.difference(keys_two):
        return 'deleted'
    is_unchanged = items_one.get(key) == items_two.get(key) or (
        isinstance(items_one.get(key), dict) and (
            isinstance(items_two.get(key), dict)
        ))
    if is_unchanged:
        return 'unchanged'
    return 'changed'


def mark_unmarked_keys(element):
    """Check dict and mark unmarked keys as 'unchanged'."""
    if not isinstance(element, dict):
        return element
    updated_dict = {}
    for key, value in element.items():  # noqa: WPS110
        updated_dict.setdefault((key, 'unchanged'), mark_unmarked_keys(value))
    return updated_dict
