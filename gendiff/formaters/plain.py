"""Contains function converting diff tree to plain output format."""


import json


def plain(diff_tree):
    """Return plain diff from diff tree."""
    return make_plain(diff_tree).rstrip()


def make_plain(diff_tree, path=''):  # noqa: WPS210
    """Generate string from diff tree."""
    diff_output = ''
    for key, keys_value in diff_tree.items():
        current_key, status = get_status_and_add_path(key, path)
        if status == 'nested':
            diff_output += make_plain(keys_value, current_key)
            continue
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
    return diff_output


def get_status_and_add_path(key, path=''):
    """Add path to a key (if needed) and set unmarked keys as 'unchanged'."""
    if path:
        new_key = f'{path}.{key[0]}'
        return new_key, key[1]
    return key


def wrap_with_quotes_and_hide_dicts(function):  # noqa: WPS231
    """Wrap string with quotes and change dict values with [complex value]."""
    def wrapper(keys_value):
        func_result = function(keys_value)
        corrected_result = []
        for element in func_result:
            if isinstance(element, dict):
                corrected_result.append('[complex value]')
                continue
            if isinstance(element, int) or element is None:
                corrected_result.append(element)
                continue
            corrected_result.append(f"'{element}'")
        return tuple(corrected_result)
    return wrapper


def dump_to_json(function):
    """Replace True/False/None with true/false/null."""
    def wrapper(keys_value):
        func_result = function(keys_value)
        corrected_result = []
        for element in func_result:
            if element in {True, False, None}:
                corrected_result.append(json.dumps(element).strip('"'))
            else:
                corrected_result.append(element)
        return tuple(corrected_result)
    return wrapper


@dump_to_json
@wrap_with_quotes_and_hide_dicts
def get_value(keys_value):
    """Return formatted value to add to output."""
    if isinstance(keys_value, tuple):
        return keys_value[1], keys_value[0]
    return keys_value, None
