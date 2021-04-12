"""Contains function converting diff tree to stylish output format."""


def stylish(diff_tree, level=0):  # noqa: WPS210
    """Generate string from diff tree."""
    if not isinstance(diff_tree, dict):
        return diff_tree
    diff_output = '{\n'
    indent = '    ' * level
    for key, keys_value in diff_tree.items():
        current_key, status = key
        old_value, current_value = get_value(keys_value, level)
        lines_template = {
            'added': f'{indent}  + {current_key}: {current_value}\n',
            'deleted': f'{indent}  - {current_key}: {current_value}\n',
            'unchanged': f'{indent}    {current_key}: {current_value}\n',
            'changed': f'{indent}  - {current_key}: {current_value}\n'  # noqa: E501, WPS221
                       f'{indent}  + {current_key}: {old_value}\n',  # noqa: E501, WPS318, WPS326
        }
        diff_output = f'{diff_output}{lines_template[status]}'
    diff_output = f'{diff_output}{indent}' + '}'  # noqa: WPS336
    return diff_output  # noqa: WPS331


def get_value(keys_value, level):
    """Return correct values to add to diff output."""
    if isinstance(keys_value, dict):
        return None, stylish(keys_value, level + 1)
    if isinstance(keys_value, tuple):
        return stylish(keys_value[1], level + 1), (
            stylish(keys_value[0], level + 1)
        )
    return None, keys_value
