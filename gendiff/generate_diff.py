"""Generate diff between two json files."""


from gendiff.parser import parse as parse_file


def generate_diff(first_file, second_file):
    """Generate diff between two files."""
    first_file = parse_file(first_file)
    second_file = parse_file(second_file)
    return stylish(find_diff(first_file, second_file))


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
            diff.setdefault(element, find_diff(
                value_one,
                second_file.get(key),
                level + 1,
            ))
        else:
            diff.setdefault(element, diff_template[status])
    return diff


def stylish(diff_tree, level=0, changed_value=''):  # noqa: WPS210
    """Generate string from diff tree."""
    if not isinstance(diff_tree, dict):
        return diff_tree
    diff_output = '{\n'
    indent = '    ' * level
    for marked_key, keys_value in diff_tree.items():
        if isinstance(marked_key, str):
            key = marked_key
            status = 'unchanged'
        else:
            key, status = marked_key
        if isinstance(keys_value, dict):
            keys_value = stylish(keys_value, level + 1)
        if isinstance(keys_value, tuple):
            changed_value = stylish(keys_value[1], level + 1)
            keys_value = stylish(keys_value[0], level + 1)
        lines_template = {
            'added': f'{diff_output}{indent}  + {key}: {keys_value}\n',
            'deleted': f'{diff_output}{indent}  - {key}: {keys_value}\n',
            'unchanged': f'{diff_output}{indent}    {key}: {keys_value}\n',
            'changed': f'{diff_output}{indent}  - {key}: {keys_value}\n'  # noqa: E501, WPS221
                       f'{indent}  + {key}: {changed_value}\n',  # noqa: E501, WPS318, WPS326
        }
        diff_output = lines_template[status]
    diff_output = f'{diff_output}{indent}' + '}'  # noqa: WPS336
    return diff_output  # noqa: WPS331


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
