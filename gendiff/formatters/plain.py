"""Contains function converting diff tree to plain output format."""


import json


def plain(diff_tree, path=''):  # noqa: WPS210, WPS231, C901
    """Return plain diff from diff tree."""
    diff_output = ''
    for key, keys_value in diff_tree.items():
        current_key, status = key if isinstance(key, tuple) else (key, None)
        current_key = f'{path}.{current_key}' if path else current_key
        if diff_output and status not in {'unchanged', None}:
            diff_output += '\n'
        if status == 'nested':
            diff_output += plain(keys_value, current_key)
        elif status == 'changed':
            current_value = format_value(keys_value[1])
            old_value = format_value(keys_value[0])
            diff_output += f"Property '{current_key}' was updated. "
            diff_output += f'From {old_value} to {current_value}'
        elif status == 'deleted':
            diff_output += f"Property '{current_key}' was removed"
        elif status == 'added':
            current_value = format_value(keys_value)
            diff_output += f"Property '{current_key}' was added with value: {current_value}"  # noqa: E501
    return diff_output


def format_value(keys_value):
    """Return formatted value to add to output."""
    if isinstance(keys_value, dict):
        return '[complex value]'
    if keys_value in {True, False, None}:
        return json.dumps(keys_value).strip('"')
    if isinstance(keys_value, int):
        return keys_value
    return f"'{keys_value}'"
