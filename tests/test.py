import os

from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


json_file1 = get_fixture_path('file1.json')
json_file2 = get_fixture_path('file2.json')
yaml_file1 = get_fixture_path('file1.yaml')
yaml_file2 = get_fixture_path('file2.yaml')



def test_return():
    assert generate_diff(json_file1, json_file2) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    assert generate_diff(yaml_file1, yaml_file2) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""