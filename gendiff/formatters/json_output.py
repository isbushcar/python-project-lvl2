"""Contains function converting diff tree to json output format."""


import json


def dump_json(diff_tree):
    """Return json string from diff tree."""
    return json.dumps(adapt_to_json(diff_tree), indent=2)


def adapt_to_json(diff_tree):  # noqa: WPS210, WPS231
    """Return dict adapted for json dump."""
    json_adapted = {}
    for key, keys_value in diff_tree.items():
        current_key, status = key if isinstance(key, tuple) else (key, None)
        if status == 'unchanged':
            continue
        if status == 'nested':
            current_value = adapt_to_json(keys_value)
            json_adapted.setdefault(current_key, current_value)
            continue
        if status == 'changed':
            old_value, current_value = keys_value
            current_value = hide_if_dict(current_value)
            old_value = hide_if_dict(old_value)
            json_adapted.setdefault(status, {})
            json_adapted[status].setdefault(
                current_key,
                [old_value, current_value],
            )
            continue
        current_value = hide_if_dict(keys_value)
        json_adapted.setdefault(status, {})
        json_adapted[status].setdefault(current_key, current_value)
    return json_adapted


def hide_if_dict(element):
    """Replace dicts with '[complex value]'."""
    if isinstance(element, dict):
        return '[complex value]'
    return element
