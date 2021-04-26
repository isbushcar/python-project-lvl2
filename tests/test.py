import os

from gendiff.generate_diff import generate_diff


def get_path(file_name, folder_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, folder_name, file_name)


def open_file(file_name, folder_name):
    return open(get_path(file_name, folder_name)).read()


def test_simple_case():
    expected_result = open_file('stylish_simple.txt', 'expected_results')
    json_file1 = get_path('file1.json', 'fixtures')
    json_file2 = get_path('file2.json', 'fixtures')
    assert generate_diff(json_file1, json_file2) == expected_result
    yaml_file1 = get_path('file1.yaml', 'fixtures')
    yaml_file2 = get_path('file2.yaml', 'fixtures')
    assert generate_diff(yaml_file1, yaml_file2) == expected_result


def test_recursive_case():
    expected_result = open_file('stylish_recursive.txt', 'expected_results')
    json_file1 = get_path('recursive_file1.json', 'fixtures')
    json_file2 = get_path('recursive_file2.json', 'fixtures')
    assert generate_diff(json_file1, json_file2) == expected_result
    yaml_file1 = get_path('recursive_file1.yaml', 'fixtures')
    yaml_file2 = get_path('recursive_file2.yaml', 'fixtures')
    assert generate_diff(yaml_file1, yaml_file2) == expected_result


def test_plain_case():
    expected_result = open_file('plain_recursive.txt', 'expected_results')
    json_file1 = get_path('recursive_file1.json', 'fixtures')
    json_file2 = get_path('recursive_file2.json', 'fixtures')
    assert generate_diff(json_file1, json_file2, 'plain') == expected_result
    yaml_file1 = get_path('recursive_file1.yaml', 'fixtures')
    yaml_file2 = get_path('recursive_file2.yaml', 'fixtures')
    assert generate_diff(yaml_file1, yaml_file2, 'plain') == expected_result


def test_simple_plain_case():
    expected_result = open_file('plain_simple.txt', 'expected_results')
    json_file1 = get_path('file1.json', 'fixtures')
    json_file2 = get_path('file2.json', 'fixtures')
    assert generate_diff(json_file1, json_file2, 'plain') == expected_result
    yaml_file1 = get_path('file1.yaml', 'fixtures')
    yaml_file2 = get_path('file2.yaml', 'fixtures')
    assert generate_diff(yaml_file1, yaml_file2, 'plain') == expected_result


def test_json_case():
    expected_result = open_file('recursive.json', 'expected_results')
    json_file1 = get_path('recursive_file1.json', 'fixtures')
    json_file2 = get_path('recursive_file2.json', 'fixtures')
    assert generate_diff(json_file1, json_file2, 'json') == expected_result
    yaml_file1 = get_path('recursive_file1.yaml', 'fixtures')
    yaml_file2 = get_path('recursive_file2.yaml', 'fixtures')
    assert generate_diff(yaml_file1, yaml_file2, 'json') == expected_result
