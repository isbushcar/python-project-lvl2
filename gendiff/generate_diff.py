"""Generate diff between two json files."""


from gendiff.parser import parse_file


def generate_diff(first_file, second_file):  # noqa: WPS210
    """Generate diff between two files."""
    first_file = parse_file(first_file)
    second_file = parse_file(second_file)
    diff = []
    for status, keys in sort_keys(first_file, second_file).items():
        for key in keys:
            diff.append(generate_diff_string(
                key, status, first_file.get(key), second_file.get(key),
            ))
    diff.sort(key=lambda element: element[4])
    diff.insert(0, '{')
    diff.append('}')
    print('\n'.join(diff))  # noqa: WPS421
    return '\n'.join(diff)


def generate_diff_string(key, status, value_one, value_two):
    """Generate string depending on key/value status."""
    string_template = {
        'added': f'  + {key}: {value_two}',
        'deleted': f'  - {key}: {value_one}',
        'unchanged': f'    {key}: {value_one}',
        'changed': f'  - {key}: {value_one}\n  + {key}: {value_two}',
    }
    return string_template[status]


def sort_keys(items_one, items_two):
    """Return dict with sorted keys (added, deleted, changed, unchanged)."""
    keys_one = set(items_one.keys())
    keys_two = set(items_two.keys())
    sorted_keys = {}
    sorted_keys.update({'added': keys_two.difference(keys_one)})
    sorted_keys.update({'deleted': keys_one.difference(keys_two)})
    sorted_keys.update({'unchanged': set(
        filter(lambda key: items_one[key] == items_two.get(key), keys_one),
    )})
    sorted_keys.update({'changed': keys_one.difference(
        sorted_keys['added'], sorted_keys['deleted'], sorted_keys['unchanged'],
    )})
    return sorted_keys
