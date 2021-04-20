"""Contains function converting diff tree to plain output format."""


import json


def plain(diff_tree, path=''):  # noqa: WPS210, WPS231, C901
    """Return plain diff from diff tree."""
    diff_output = ''
    for key, keys_value in diff_tree.items():
        if not isinstance(key, tuple) or key[1] == 'unchanged':
            continue
        if diff_output:
            diff_output += '\n'
        current_key, status = key
        current_key = f'{path}.{current_key}' if path else current_key
        if status == 'nested':
            diff_output += plain(keys_value, current_key)
            continue
        if status == 'changed':
            current_value = format_value(keys_value[1])
            old_value = format_value(keys_value[0])
            diff_output += f"Property '{current_key}' was updated. "
            diff_output += f'From {old_value} to {current_value}'
            continue
        current_value = format_value(keys_value)
        if status == 'deleted':
            diff_output += f"Property '{current_key}' was removed"
            continue
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
