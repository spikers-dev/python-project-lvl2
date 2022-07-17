from gendiff.libs.diff_flat import generate_diff
from gendiff.libs.diff_parser import load_file
import tests.expected as expected


file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yaml'
file_nofound = 'tests/fixtures/file_nofound.yaml'
file_unformat = 'tests/fixtures/file_unformat.txt'
file1_compl_json = 'tests/fixtures/file1_complex.json'
file2_compl_json = 'tests/fixtures/file2_complex.json'
file1_compl_yaml = 'tests/fixtures/file1_complex.yaml'
file2_compl_yaml = 'tests/fixtures/file2_complex.yaml'


def test1_simple_json_work():
    actual = generate_diff(file1_json, file2_json)
    assert actual == expected.SIMPLE_STRING


def test2_simple_yaml_work():
    actual = generate_diff(file1_yaml, file2_yaml)
    assert actual == expected.SIMPLE_STRING


def test3_parser_empty():
    actual = load_file(file_nofound)
    assert str(actual)[:9] == expected.ERROR_MSG01


# def test4_parser_unformat():
#     actual = load_file(file_unformat)
#     assert str(actual)[:29] == expected.ERROR_MSG02


def test4_complex_json_work():
    actual = generate_diff(file1_compl_json, file2_compl_json)
    assert actual == expected.COMPLEX_STRING


def test5_complex_yaml_work():
    actual = generate_diff(file1_compl_yaml, file2_compl_yaml)
    assert actual == expected.COMPLEX_STRING


def test6_complex_json_plain():
    actual = generate_diff(file1_compl_json, file2_compl_json, 'plain')
    assert actual == expected.PLAIN_COMP_STRING


def test7_simple_json_plain():
    actual = generate_diff(file1_json, file2_json, 'plain')
    assert actual == expected.PLAIN_STRING
