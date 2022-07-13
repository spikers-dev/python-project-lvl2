from gendiff.libs.diff_flat import generate_diff
import tests.expected as expected


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'


def test1_simple_work():
    actual = generate_diff(file1, file2)
    assert actual == expected.SIMPLE_STRING
