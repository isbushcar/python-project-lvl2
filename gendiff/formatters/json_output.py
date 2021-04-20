"""Contains function converting diff tree to json output format."""


import json


def dump_json(diff_tree):
    """Return json string from diff tree."""
    return json.dumps(diff_tree, indent=2)
