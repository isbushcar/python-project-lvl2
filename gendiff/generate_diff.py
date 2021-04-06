"""Generate diff between two json files."""


from gendiff.parser import parse as parse_file


def generate_diff(first_file, second_file):
    """Generate diff between two files."""
    first_file = parse_file(first_file)
    second_file = parse_file(second_file)
    return find_diff(first_file, second_file)


def find_diff(first_file, second_file, level=0):  # noqa: WPS210
    """Find difference between data in two objects."""
    diff = []
    for status, keys in sort_keys(first_file, second_file).items():
        for key in keys:
            are_both_dicts = isinstance(first_file.get(key), dict) and (
                isinstance(second_file.get(key), dict)
            )
            if are_both_dicts:
                inner_diff = find_diff(
                    first_file.get(key),
                    second_file.get(key),
                    level + 1,
                )
                diff.append(generate_diff_lines(
                    key,
                    status,
                    inner_diff,
                    level=level,
                ))
            else:
                diff.append(generate_diff_lines(
                    key,
                    status,
                    first_file.get(key),
                    second_file.get(key),
                    level=level,
                ))
    diff.sort(key=strip_string_to_sort)
    diff.insert(0, '{')
    diff.append('    ' * level + '}')  # noqa: WPS336
    print('\n'.join(diff))  # noqa: WPS421
    return '\n'.join(diff)


def generate_diff_lines(key, status, value_one, value_two='', level=0):
    """Generate string depending on key/value status."""
    indent = '    ' * level
    if isinstance(value_one, dict):
        value_one = dict_to_string(value_one, level + 1)
    if isinstance(value_two, dict):
        value_two = dict_to_string(value_two, level + 1)
    string_template = {
        'added': f'{indent}  + {key}: {value_two}',
        'deleted': f'{indent}  - {key}: {value_one}',
        'unchanged': f'{indent}    {key}: {value_one}',
        'changed': f'{indent}  - {key}: {value_one}\n'   # noqa: WPS221, WPS326
                   f'{indent}  + {key}: {value_two}',  # noqa: WPS318, WPS326
    }
    return string_template[status]


def sort_keys(items_one, items_two):
    """Return dict with sorted keys (added, deleted, changed, unchanged)."""
    keys_one = set(items_one.keys())
    keys_two = set(items_two.keys())
    sorted_keys = {}
    sorted_keys.update({'added': keys_two.difference(keys_one)})
    sorted_keys.update({'deleted': keys_one.difference(keys_two)})
    sorted_keys.update({'unchanged': set(
        filter(lambda key: is_unchanged(items_one, items_two, key), keys_one),
    )})
    sorted_keys.update({'changed': keys_one.difference(
        sorted_keys['added'], sorted_keys['deleted'], sorted_keys['unchanged'],
    )})
    return sorted_keys


def is_unchanged(items_one, items_two, key):
    """Return True if values are dictionaries or equal to each other."""
    if items_one.get(key) == items_two.get(key):
        return True
    return isinstance(items_one.get(key), dict) and (
        isinstance(items_two.get(key), dict)
    )


def strip_string_to_sort(string):
    """Delete spaces, + and - in start of the line."""
    return string.lstrip().lstrip('-').lstrip('+').lstrip()


def dict_to_string(dict_to_convert, level):
    """Convert dict into a string (for added or deleted keys)."""
    string = '{\n'
    for key, value in dict_to_convert.items():  # noqa: WPS110
        local_indent = '    ' * (level + 1)
        if isinstance(value, dict):
            converted_value = dict_to_string(value, level + 1)
            string = f'{string}{local_indent}{key}: {converted_value}\n'
        else:
            string = f'{string}{local_indent}{key}: {value}\n'
    string = string + ('    ' * level) + '}'  # noqa: WPS336
    return string  # noqa: WPS331
