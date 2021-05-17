from gendiff.generate_diff import generate_diff, PLAIN, JSON


def test_simple_case(json_files, yaml_files, stylish_simple_result):
    expected_result = open(stylish_simple_result).read()
    assert generate_diff(json_files[0], json_files[1]) == expected_result
    assert generate_diff(yaml_files[0], yaml_files[1]) == expected_result


def test_recursive_case(recursive_json_files, recursive_yaml_files, stylish_recursive_result):
    expected_result = open(stylish_recursive_result).read()
    assert generate_diff(recursive_json_files[0], recursive_json_files[1]) == expected_result
    assert generate_diff(recursive_yaml_files[0], recursive_yaml_files[1]) == expected_result


def test_plain_case(recursive_json_files, recursive_yaml_files, plain_recursive_result):
    expected_result = open(plain_recursive_result).read()
    assert generate_diff(recursive_json_files[0], recursive_json_files[1], PLAIN) == expected_result
    assert generate_diff(recursive_yaml_files[0], recursive_yaml_files[1], PLAIN) == expected_result


def test_simple_plain_case(json_files, yaml_files, plain_simple_result):
    expected_result = open(plain_simple_result).read()
    assert generate_diff(json_files[0], json_files[1], PLAIN) == expected_result
    assert generate_diff(yaml_files[0], yaml_files[1], PLAIN) == expected_result


def test_json_case(recursive_json_files, recursive_yaml_files, json_result):
    expected_result = open(json_result).read()
    assert generate_diff(recursive_json_files[0], recursive_json_files[1], JSON) == expected_result
    assert generate_diff(recursive_yaml_files[0], recursive_yaml_files[1], JSON) == expected_result
