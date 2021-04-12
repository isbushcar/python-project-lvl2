import os

from gendiff.formaters.json_output import dump_json
from gendiff.formaters.plain import plain
from gendiff.generate_diff import generate_diff


def get_path(file_name, folder_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, folder_name, file_name)


def test_simple_case():
    simple_case_result = open(get_path('simple_case_result', 'expected_results')).read()
    json_file1 = get_path('file1.json', 'fixtures')
    json_file2 = get_path('file2.json', 'fixtures')
    assert generate_diff(json_file1, json_file2) == simple_case_result
    yaml_file1 = get_path('file1.yaml', 'fixtures')
    yaml_file2 = get_path('file2.yaml', 'fixtures')
    assert generate_diff(yaml_file1, yaml_file2) == simple_case_result


def test_recursive_case():
    recursive_case_result = open(get_path('recursive_case_result', 'expected_results')).read()
    json_recursive_file1 = get_path('recursive_file1.json', 'fixtures')
    json_recursive_file2 = get_path('recursive_file2.json', 'fixtures')
    assert generate_diff(json_recursive_file1, json_recursive_file2) == recursive_case_result
    yaml_recursive_file1 = get_path('recursive_file1.yaml', 'fixtures')
    yaml_recursive_file2 = get_path('recursive_file2.yaml', 'fixtures')
    assert generate_diff(yaml_recursive_file1, yaml_recursive_file2) == recursive_case_result


def test_plain_case():
    plain_case_result = open(get_path('plain_case_result', 'expected_results')).read()
    json_recursive_file1 = get_path('recursive_file1.json', 'fixtures')
    json_recursive_file2 = get_path('recursive_file2.json', 'fixtures')
    assert generate_diff(json_recursive_file1, json_recursive_file2, 'plain') == plain_case_result
    yaml_recursive_file1 = get_path('recursive_file1.yaml', 'fixtures')
    yaml_recursive_file2 = get_path('recursive_file2.yaml', 'fixtures')
    assert generate_diff(yaml_recursive_file1, yaml_recursive_file2, 'plain') == plain_case_result


def test_json_case():
    json_case_result = open(get_path('json_case_result', 'expected_results')).read()
    json_recursive_file1 = get_path('recursive_file1.json', 'fixtures')
    json_recursive_file2 = get_path('recursive_file2.json', 'fixtures')
    assert generate_diff(json_recursive_file1, json_recursive_file2, 'json') == json_case_result
    yaml_recursive_file1 = get_path('recursive_file1.yaml', 'fixtures')
    yaml_recursive_file2 = get_path('recursive_file2.yaml', 'fixtures')
    assert generate_diff(yaml_recursive_file1, yaml_recursive_file2, 'json') == json_case_result


if __name__ == '__main__':
    test_simple_case()
    test_recursive_case()
    test_plain_case()
    test_json_case()
