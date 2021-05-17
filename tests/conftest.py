import os
import pytest


TESTS_DIR = os.path.join(os.getcwd(), 'tests')


# @pytest.fixture
# def expected_result(case_name):
#     fixture_list = {
#         'stylish_simple': 'stylish_simple.txt',
#         'stylish_recursive': 'stylish_recursive.txt',
#         'plain_recursive': 'plain_recursive.txt',
#         'plain_simple': 'plain_simple.txt',
#         'json': 'recursive.json',
#     }
#     return os.path.join(CWD, 'expected_results', fixture_list[case_name])


@pytest.fixture
def fixture_list():
    return [
        (json_files, stylish_simple_result, 'stylish'),
        (yaml_files, stylish_simple_result, 'stylish'),
        (recursive_json_files, stylish_recursive_result, 'stylish'),
        (recursive_yaml_files, stylish_recursive_result, 'stylish'),
        (recursive_json_files, plain_recursive_result, 'plain'),
        (recursive_yaml_files, plain_recursive_result, 'plain'),
        (json_files, plain_simple_result, 'plain'),
        (yaml_files, plain_simple_result, 'plain'),
        (recursive_json_files, json_result, 'json'),
        (recursive_yaml_files, json_result, 'json'),
    ]


@pytest.fixture
def stylish_simple_result():
    return os.path.join(TESTS_DIR, 'expected_results', 'stylish_simple.txt')


@pytest.fixture
def stylish_recursive_result():
    return os.path.join(TESTS_DIR, 'expected_results', 'stylish_recursive.txt')


@pytest.fixture
def plain_recursive_result():
    return os.path.join(TESTS_DIR, 'expected_results', 'plain_recursive.txt')


@pytest.fixture
def plain_simple_result():
    return os.path.join(TESTS_DIR, 'expected_results', 'plain_simple.txt')


@pytest.fixture
def json_result():
    return os.path.join(TESTS_DIR, 'expected_results', 'recursive.json')


@pytest.fixture
def json_files():
    return (
        os.path.join(TESTS_DIR, 'fixtures', 'file1.json'),
        os.path.join(TESTS_DIR, 'fixtures', 'file2.json'),
    )


@pytest.fixture
def yaml_files():
    return (
        os.path.join(TESTS_DIR, 'fixtures', 'file1.yaml'),
        os.path.join(TESTS_DIR, 'fixtures', 'file2.yaml'),
    )


@pytest.fixture
def recursive_yaml_files():
    return (
        os.path.join(TESTS_DIR, 'fixtures', 'recursive_file1.yaml'),
        os.path.join(TESTS_DIR, 'fixtures', 'recursive_file2.yaml'),
    )


@pytest.fixture
def recursive_json_files():
    return (
        os.path.join(TESTS_DIR, 'fixtures', 'recursive_file1.json'),
        os.path.join(TESTS_DIR, 'fixtures', 'recursive_file2.json'),
    )
