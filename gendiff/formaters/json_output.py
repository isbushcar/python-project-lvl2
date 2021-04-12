"""Contains function converting diff tree to json output format."""
import json

def json_output(diff_tree, path=()):  # noqa: WPS210
    """Generate string from diff tree."""
    if not isinstance(diff_tree, dict):
        return diff_tree
    # diff_output = '{\n'
    # indent = '    ' * level
    json_adapted = {}
    for key, keys_value in diff_tree.items():
        
        current_key, status = key
        old_value, current_value = get_value(keys_value, path=()
        json_adapted.setdefault(current_key, current_value)
        #json_adapted[status].setdefault(current_key, current_value)
        # json_adapted[status].setdefault(current_key, current_value)
    #return json_adapted
    return json.dumps(json_adapted, indent=2)
            # lines_template[status].append(f'{current_key}: {current_value}\n')
    # return added_keys, deleted_keys, changed_keys


def get_value(keys_value, level):
    """Return correct values to add to diff output."""
    if isinstance(keys_value, dict):
        return None, json_output(keys_value)
    if isinstance(keys_value, tuple):
        return json_output(keys_value[1], level + 1), (
            json_output(keys_value[0], level + 1)
        )
    return None, keys_value


a = {('common', 'unchanged'): {('follow', 'added'): 'false', ('setting1', 'unchanged'): 'Value 1', ('setting2', 'deleted'): '200', ('setting3', 'changed'): ('true', 'null'), ('setting4', 'added'): 'blah blah', ('setting5', 'added'): {('key5', 'unchanged'): 'value5'}, ('setting6', 'unchanged'): {('doge', 'unchanged'): {('wow', 'changed'): ('', 'so much')}, ('key', 'unchanged'): 'value', ('ops', 'added'): 'vops'}}, ('group1', 'unchanged'): {('baz', 'changed'): ('bas', 'bars'), ('foo', 'unchanged'): 'bar', ('nest', 'changed'): ({('key', 'unchanged'): 'value'}, 'str')}, ('group2', 'deleted'): {('abc', 'unchanged'): '12345', ('deep', 'unchanged'): {('id', 'unchanged'): '45'}}, ('group3', 'added'): {('deep', 'unchanged'): {('id', 'unchanged'): {('number', 'unchanged'): '45'}}, ('fee', 'unchanged'): '100500'}}
print(json_output(a))
# print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], indent=2))