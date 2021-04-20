"""Contains function converting diff tree to stylish output format."""


import json


def stylish(diff_tree, level=0):  # noqa: WPS210
    """Generate string from diff tree."""
    diff_output = '{\n'
    indent = '    ' * level
    for key, keys_value in diff_tree.items():
        current_key, status = key if isinstance(key, tuple) else (key, None)
        if status == 'nested':
            inner_diff = stylish(keys_value, level + 1)
            diff_output += f'{indent}    {current_key}: {inner_diff}\n'
        else:
            current_value, old_value = get_value(keys_value, level + 1)
            lines_template = {
                'added': f'{indent}  + {current_key}: {current_value}\n',
                'deleted': f'{indent}  - {current_key}: {current_value}\n',
                'unchanged': f'{indent}    {current_key}: {current_value}\n',
                'changed': f'{indent}  - {current_key}: {current_value}\n'  # noqa: E501, WPS221
                           f'{indent}  + {current_key}: {old_value}\n',  # noqa: E501, WPS318, WPS326
                None: f'{indent}    {current_key}: {current_value}\n',
            }
            diff_output += lines_template[status]
    diff_output += indent + '}'
    return diff_output


def get_value(keys_value, level=1):
    """Return correct values to add to diff output."""
    if isinstance(keys_value, tuple):
        return get_value(keys_value[0], level)[0], (
            get_value(keys_value[1], level)[0]
        )
    if not isinstance(keys_value, dict):
        return json.dumps(keys_value).strip('"'), None
    inner_diff = '{\n'
    indent = '    ' * level
    for inner_key, inner_value in keys_value.items():
        if isinstance(inner_value, dict):
            inner_value = get_value(inner_value, level + 1)[0]
        inner_diff += f'{indent}    {inner_key}: {inner_value}\n'
    inner_diff += indent + '}'
    return inner_diff, None
