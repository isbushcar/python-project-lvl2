"""Contains function converting diff tree to stylish output format."""


import json


def stylish(diff_tree):  # noqa: WPS210
    """Generate string from diff tree."""
    diff_output = '{\n'
    for key, keys_value in diff_tree.items():
        current_key, status = get_key_and_status(key)
        current_value, old_value = get_value(keys_value)
        diff_output += generate_diff_string(
            current_key,
            status,
            current_value,
            old_value,
        )
    diff_output += '}'  # noqa: WPS336
    return diff_output


def get_value(keys_value, level=1):  # noqa: WPS210
    """Return correct values to add to diff output."""
    if isinstance(keys_value, tuple):
        return get_value(keys_value[0], level)[0], (
            get_value(keys_value[1], level)[0]
        )
    if not isinstance(keys_value, dict):
        return json.dumps(keys_value).strip('"'), None
    inner_diff = '{\n'
    for inner_key, inner_value in keys_value.items():
        current_key, status = get_key_and_status(inner_key)
        current_value, old_value = get_value(inner_value, level + 1)
        inner_diff += generate_diff_string(
            current_key,
            status,
            current_value,
            old_value,
            level,
        )
    inner_diff += '    ' * level + '}'  # noqa: WPS336
    return inner_diff, None


def get_key_and_status(key):
    """Return key and its status (unmarked keys get status 'unchanged'."""
    if isinstance(key, tuple):
        return key[0], key[1]
    return key, 'unchanged'


def generate_diff_string(current_key, status, current_value, old_value, level=0):  # noqa: E501
    """Return generated diff string to add to output."""
    indent = '    ' * level
    lines_template = {
        'added': f'{indent}  + {current_key}: {current_value}\n',
        'deleted': f'{indent}  - {current_key}: {current_value}\n',
        'unchanged': f'{indent}    {current_key}: {current_value}\n',
        'nested': f'{indent}    {current_key}: {current_value}\n',
        'changed': f'{indent}  - {current_key}: {current_value}\n'  # noqa: E501, WPS221
                   f'{indent}  + {current_key}: {old_value}\n',  # noqa: E501, WPS318, WPS326
    }
    return lines_template[status]
