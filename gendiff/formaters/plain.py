"""Contains function converting diff tree to plain output format."""


def plain(diff_tree, path=''):  # noqa: WPS210
    """Generate string from diff tree."""
    diff_output = ''
    for key, keys_value in diff_tree.items():
        current_key, status = add_mark_and_path(key, path)
        if isinstance(keys_value, dict):
            diff_output += plain(keys_value, current_key)
        current_value, old_value = get_value(keys_value)
        lines_template = {
            'added': f"Property '{current_key}' was added with value: "
                     f'{current_value}\n',  # noqa: WPS318, WPS326
            'deleted': f"Property '{current_key}' was removed\n",
            'unchanged': '',
            'changed': f"Property '{current_key}' was updated. "
                       f'From {old_value} to {current_value}\n',  # noqa: WPS318, WPS326, E501
        }
        diff_output = f'{diff_output}{lines_template[status]}'
    return diff_output  # noqa: WPS331


def add_mark_and_path(key, path=''):
    """Add path to a key (if needed) and mark unmarked keys as 'unchanged'."""
    if isinstance(key, str):
        return f'{path}.{key}' if path else key, 'unchanged'
    if path:
        new_key = f'{path}.{key[0]}'
        return new_key, key[1]
    return key


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
