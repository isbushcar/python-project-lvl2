"""Contains function converting diff tree to stylish output format."""


import json

INDENT = ' ' * 4
COLON = ': '


def stylish(diff_tree, level=0):  # noqa: WPS210, WPS231
    """Generate string from diff tree."""
    diff_output = '{\n'
    indent = INDENT * level
    for key, keys_value in diff_tree.items():
        current_key, status = key if isinstance(key, tuple) else (key, None)
        if status == 'nested':
            inner_diff = stylish(keys_value, level + 1)
            diff_output += f'{indent}{INDENT}{current_key}{COLON}{inner_diff}\n'
        elif status == 'changed':
            old_value = get_value(keys_value[0], level + 1)
            current_value = get_value(keys_value[1], level + 1)
            diff_output += f'{indent}  - {current_key}{COLON}{old_value}\n'
            diff_output += f'{indent}  + {current_key}{COLON}{current_value}\n'
        else:
            current_value = get_value(keys_value, level + 1)
            if status == 'added':
                diff_output += f'{indent}  + {current_key}{COLON}{current_value}\n'  # noqa: E501
            elif status == 'deleted':
                diff_output += f'{indent}  - {current_key}{COLON}{current_value}\n'  # noqa: E501
            else:
                diff_output += f'{indent}{INDENT}{current_key}{COLON}{current_value}\n'  # noqa: E501
    diff_output += indent + '}'
    return diff_output


def get_value(keys_value, level=1):
    """Return correct values to add to diff output."""
    if not isinstance(keys_value, dict):
        return json.dumps(keys_value).strip('"')
    inner_diff = '{\n'
    indent = INDENT * level
    for inner_key, inner_value in keys_value.items():
        if isinstance(inner_value, dict):
            inner_value = get_value(inner_value, level + 1)
        inner_diff += f'{indent}{INDENT}{inner_key}{COLON}{inner_value}\n'
    inner_diff += indent + '}'
    return inner_diff
