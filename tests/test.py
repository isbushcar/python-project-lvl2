import os

from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


file1 = get_fixture_path('file1.json')
file2 = get_fixture_path('file2.json')


def test_return():
    assert generate_diff(file1, file2) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
