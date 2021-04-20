"""Contains function converting diff tree to plain output format."""


import json


def plain(diff_tree, path=''):  # noqa: WPS210, WPS231
    """Return plain diff from diff tree."""
    diff_output = ''
    for key, keys_value in diff_tree.items():
        current_key, status = key if isinstance(key, tuple) else (key, None)
        if diff_output and status is not None and status != 'unchanged':
            diff_output += '\n'
        current_key = f'{path}.{current_key}' if path else current_key
        if status == 'nested':
            diff_output += plain(keys_value, current_key)
            continue
        if status == 'changed':
            current_value = get_value(keys_value[1])
            old_value = get_value(keys_value[0])
            diff_output += f"Property '{current_key}' was updated. "
            diff_output += f'From {old_value} to {current_value}'
            continue
        keys_value = get_value(keys_value)
        lines_template = {
            'added': f"Property '{current_key}' was added with value: "
                     f'{keys_value}',  # noqa: WPS318, WPS326
            'deleted': f"Property '{current_key}' was removed",
            'unchanged': '',
            None: '',
        }
        diff_output = f'{diff_output}{lines_template[status]}'
    return diff_output


def get_value(keys_value):
    """Return formatted value to add to output."""
    if isinstance(keys_value, dict):
        return '[complex value]'
    if keys_value in {True, False, None}:
        return json.dumps(keys_value).strip('"')
    if isinstance(keys_value, int):
        return keys_value
    return f"'{keys_value}'"
