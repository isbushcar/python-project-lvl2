import os

from gendiff_package.formaters.json_output import dump_json
from gendiff_package.formaters.plain import plain
from gendiff import generate_diff

from tests.expected_results import *


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


json_file1 = get_fixture_path('file1.json')
json_file2 = get_fixture_path('file2.json')
yaml_file1 = get_fixture_path('file1.yaml')
yaml_file2 = get_fixture_path('file2.yaml')
json_recursive_file1 = get_fixture_path('recursive_file1.json')
json_recursive_file2 = get_fixture_path('recursive_file2.json')
yaml_recursive_file1 = get_fixture_path('recursive_file1.yaml')
yaml_recursive_file2 = get_fixture_path('recursive_file2.yaml')


def test_return():
    assert generate_diff(json_file1, json_file2) == simple_case_result
    assert generate_diff(yaml_file1, yaml_file2) == simple_case_result
    assert generate_diff(
        json_recursive_file1, json_recursive_file2) == compl_case_result
    assert generate_diff(
        yaml_recursive_file1, yaml_recursive_file2) == compl_case_result
    assert generate_diff(
        json_recursive_file1, json_recursive_file2, plain) == plain_case_result
    assert generate_diff(
        yaml_recursive_file1, yaml_recursive_file2, plain) == plain_case_result
    assert generate_diff(
        json_recursive_file1, json_recursive_file2, dump_json) == json_case_result
    assert generate_diff(
        yaml_recursive_file1, yaml_recursive_file2, dump_json) == json_case_result


if __name__ == '__main__':
    test_return()
