"""Generate diff between two json files."""

from gendiff.formatter import stylish
from gendiff.parser import load_file_content


def generate_diff(first_file, second_file, formatter=stylish):
    """Generate diff between two files."""
    first_file = load_file_content(first_file)
    second_file = load_file_content(second_file)
    print(find_diff(first_file, second_file))  # noqa: WPS421
    return formatter(find_diff(first_file, second_file))


def find_diff(first_file, second_file, level=0):  # noqa: WPS210
    """Find difference between data in two objects."""
    key_list = mark_keys(first_file, second_file)
    diff = {}
    for element in key_list:
        key, status = element
        value_one = first_file.get(key)
        value_two = second_file.get(key)
        diff_template = {
            'added': value_two,
            'deleted': value_one,
            'unchanged': value_one,
            'changed': (value_one, value_two),
        }
        if isinstance(value_one, dict) and isinstance(value_two, dict):
            dict_diff = find_diff(value_one, second_file.get(key), level + 1)
            diff.setdefault(element, dict_diff)
            continue
        diff.setdefault(element, diff_template[status])
    return diff


def mark_keys(items_one, items_two):
    """Return sorted list with marked keys (added/deleted/changed/unchanged)."""
    keys_one = set(items_one.keys())
    keys_two = set(items_two.keys())
    marked_keys = []
    keys = keys_one.union(keys_two)
    for key in keys:
        if key in keys_two.difference(keys_one):
            marked_keys.append((key, 'added'))
        elif key in keys_one.difference(keys_two):
            marked_keys.append((key, 'deleted'))
        elif is_unchanged(items_one, items_two, key):
            marked_keys.append((key, 'unchanged'))
        else:
            marked_keys.append((key, 'changed'))
    marked_keys.sort(key=lambda marked_key: marked_key[0])
    return marked_keys


def is_unchanged(items_one, items_two, key):
    """Return True if values are dictionaries or equal to each other."""
    if items_one.get(key) == items_two.get(key):
        return True
    return isinstance(items_one.get(key), dict) and (
        isinstance(items_two.get(key), dict)
    )
