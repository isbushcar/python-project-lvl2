"""Contains function converting diff tree to json output format."""


import json


def dump_json(diff_tree):
    """Return json string from diff tree."""
    return json.dumps(adapt_to_json(diff_tree), indent=2)


def adapt_to_json(diff_tree):  # noqa: WPS210
    """Return dict adapted for json dump."""
    if not isinstance(diff_tree, dict):
        return diff_tree
    json_adapted = {}
    for key, keys_value in diff_tree.items():
        current_key, status = get_key_and_status(key)
        items_to_add = get_items_to_add(current_key, status, keys_value)
        if items_to_add is None:
            continue
        if status in {'unchanged', 'nested'}:
            json_adapted.setdefault(*items_to_add)
            continue
        json_adapted.setdefault(status, {})
        json_adapted[status].setdefault(*items_to_add)
    return json_adapted


def get_items_to_add(current_key, status, keys_value):
    """Return keys and values to add."""
    old_value, current_value = get_value(keys_value)
    if status == 'unchanged':
        return None
    if status == 'nested':
        return current_key, current_value
    if status == 'changed':
        return current_key, [hide_dicts(old_value), hide_dicts(current_value)]
    return current_key, hide_dicts(current_value)


def hide_dicts(element):
    """Change inner dict with string '[complex value]'."""
    if isinstance(element, dict):
        return '[complex value]'
    return element


def get_value(keys_value):
    """Return correct values to add to diff output."""
    if isinstance(keys_value, dict):
        return None, adapt_to_json(keys_value)
    if isinstance(keys_value, tuple):
        return adapt_to_json(keys_value[1]), (
            adapt_to_json(keys_value[0])
        )
    return None, keys_value


def get_key_and_status(key):
    """Return key and its status (unmarked keys get status 'unchanged'."""
    if isinstance(key, tuple):
        return key[0], key[1]
    return key, 'unchanged'
