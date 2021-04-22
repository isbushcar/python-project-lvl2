"""Contains function converting diff tree to stylish output format."""


import json

INDENT = ' ' * 4
COLON = ': '


def stylish(diff_tree, level=0):  # noqa: WPS210, WPS231
    """Generate string from diff tree."""
    diff_output = '{\n'
    indent = INDENT * level
    inner_lvl = level + 1
    for key, inner_keys in diff_tree.items():
        status = inner_keys.get('status')
        keys_value = inner_keys['value']
        if status == 'nested':
            inner_diff = stylish(keys_value, inner_lvl)
            diff_output += f'{indent}{INDENT}{key}{COLON}{inner_diff}\n'
        elif status == 'changed':
            old_value = get_formatted_value(keys_value['old value'], inner_lvl)
            new_value = get_formatted_value(keys_value['new value'], inner_lvl)
            diff_output += f'{indent}  - {key}{COLON}{old_value}\n'
            diff_output += f'{indent}  + {key}{COLON}{new_value}\n'
        elif status == 'added':
            current_value = get_formatted_value(keys_value, inner_lvl)
            diff_output += f'{indent}  + {key}{COLON}{current_value}\n'
        elif status == 'deleted':
            current_value = get_formatted_value(keys_value, inner_lvl)
            diff_output += f'{indent}  - {key}{COLON}{current_value}\n'
        else:
            current_value = get_formatted_value(keys_value, inner_lvl)
            diff_output += f'{indent}{INDENT}{key}{COLON}{current_value}\n'
    diff_output += indent + '}'
    return diff_output


def get_formatted_value(keys_value, level=1):
    """Return value (as a string) to add to diff output."""
    if not isinstance(keys_value, dict):
        return json.dumps(keys_value).strip('"')
    formatted_value = '{\n'
    indent = INDENT * level
    for inner_key, inner_value in keys_value.items():
        inner_value = get_formatted_value(inner_value, level + 1)
        formatted_value += f'{indent}{INDENT}{inner_key}{COLON}{inner_value}\n'
    formatted_value += indent + '}'
    return formatted_value
