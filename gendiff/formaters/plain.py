"""Contains function converting diff tree to plain output format."""


def plain(diff_tree, path=''):  # noqa: WPS210
    """Generate string from diff tree."""
    diff_output = ''
    for marked_key, keys_value in diff_tree.items():
        key, status = get_key_and_status(marked_key)
        key = f'{path}.{key}' if path else key
        if isinstance(keys_value, dict):
            diff_output += plain(keys_value, key)
        current_value, old_value = get_value(keys_value)
        lines_template = {
            'added': f"Property '{key}' was added with value: "
                     f'{current_value}\n',  # noqa: WPS318, WPS326
            'deleted': f"Property '{key}' was removed\n",
            'unchanged': '',
            'changed': f"Property '{key}' was updated. "
                       f'From {old_value} to {current_value}\n',  # noqa: WPS318, WPS326, E501
        }
        diff_output = f'{diff_output}{lines_template[status]}'
    return diff_output  # noqa: WPS331


def get_key_and_status(marked_key):
    """Return key and its status. Unmarked keys get status 'unchanged'."""
    if isinstance(marked_key, str):
        return marked_key, 'unchanged'
    return marked_key


def wrap_with_quotes_and_hide_dicts(function):
    """Wrap string with quotes and change dict values with [complex value]."""
    def wrapper(keys_value):
        stop_list = {'true', 'false', 'null'}
        func_result = function(keys_value)
        corrected_result = []
        for element in func_result:
            if isinstance(element, dict):
                corrected_result.append('[complex value]')
            elif element in stop_list:
                corrected_result.append(element)
            else:
                corrected_result.append(f"'{element}'")
        return tuple(corrected_result)
    return wrapper


@wrap_with_quotes_and_hide_dicts
def get_value(keys_value):
    """Return formatted value to add to output."""
    if isinstance(keys_value, tuple):
        return keys_value[1], keys_value[0]
    return keys_value, None
