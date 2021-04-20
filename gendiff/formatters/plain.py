"""Contains function converting diff tree to plain output format."""


import json


def plain(diff_tree, path=''):  # noqa: WPS210, WPS231, C901
    """Return plain diff from diff tree."""
    diff_output = ''
    for key, _ in diff_tree.items():
        status = diff_tree[key].get('status')
        keys_value = diff_tree[key]['value']
        current_key = f'{path}.{key}' if path else key
        if status == 'nested':
            diff_output += plain(keys_value, current_key) + '\n'
        elif status == 'changed':
            current_value = get_formatted_value(keys_value['new value'])
            old_value = get_formatted_value(keys_value['old value'])
            diff_output += f"Property '{current_key}' was updated. "
            diff_output += f'From {old_value} to {current_value}\n'
        elif status == 'deleted':
            diff_output += f"Property '{current_key}' was removed\n"
        elif status == 'added':
            current_value = get_formatted_value(keys_value)
            diff_output += f"Property '{current_key}' was added with value: {current_value}\n"  # noqa: E501
    return diff_output.rstrip()


def get_formatted_value(keys_value):
    """Return formatted value to add to output."""
    if isinstance(keys_value, dict):
        return '[complex value]'
    if keys_value in {True, False, None}:
        return json.dumps(keys_value).strip('"')
    if isinstance(keys_value, int):
        return keys_value
    return f"'{keys_value}'"
