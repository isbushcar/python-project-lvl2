"""Contains function converting diff tree to output format."""


def stylish(diff_tree, level=0, changed_value=''):  # noqa: WPS210
    """Generate string from diff tree."""
    if not isinstance(diff_tree, dict):
        return diff_tree
    diff_output = '{\n'
    indent = '    ' * level
    for marked_key, keys_value in diff_tree.items():
        key, status = get_key_and_status(marked_key)
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


def get_key_and_status(marked_key):
    """Return key and its status. Unmarked keys get status 'unchanged'."""
    if isinstance(marked_key, str):
        return marked_key, 'unchanged'
    return marked_key
