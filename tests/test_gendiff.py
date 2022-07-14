from gendiff.libs.diff_flat import generate_diff
import tests.expected as expected


file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yaml'


def test1_simple_json_work():
    actual = generate_diff(file1_json, file2_json)
    assert actual == expected.SIMPLE_STRING


def test2_simple_yaml_work():
    actual = generate_diff(file1_yaml, file2_yaml)
    assert actual == expected.SIMPLE_STRING
