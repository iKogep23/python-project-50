import pytest
from gendiff.diff import generate_diff
from gendiff.file_reader import read_file, get_format
from gendiff.parser import parse
from gendiff.formatters import formatter_foo


FLAT_JSON_FILE1 = 'tests/fixtures/file1.json'
FLAT_JSON_FILE2 = 'tests/fixtures/file2.json'
FLAT_YAML_FILE1 = 'tests/fixtures/file1.yaml'
FLAT_YAML_FILE2 = 'tests/fixtures/file2.yaml'
FLAT_YML_FILE1 = 'tests/fixtures/file1.yml'
FLAT_YML_FILE2 = 'tests/fixtures/file2.yml'
NESTED_JSON_FILE1 = 'tests/fixtures/file1_nested.json'
NESTED_JSON_FILE2 = 'tests/fixtures/file2_nested.json'
NESTED_YAML_FILE1 = 'tests/fixtures/file1_nested.yaml'
NESTED_YAML_FILE2 = 'tests/fixtures/file2_nested.yaml'

ANSWER_STYLISH_FLAT = 'tests/fixtures/answer_stylish_flat'
ANSWER_STYLISH_NESTED = 'tests/fixtures/answer_stylish_nested'
ANSWER_PLAIN_FLAT = 'tests/fixtures/answer_plain_flat'
ANSWER_PLAIN_NESTED = 'tests/fixtures/answer_plain_nested'
ANSWER_JSON_FLAT = 'tests/fixtures/answer_json_flat'
ANSWER_JSON_NESTED = 'tests/fixtures/answer_json_nested'


def test_get_format_raises_exception():
    """Test the exception handle in get_format function."""
    with pytest.raises(ValueError):
        get_format(ANSWER_PLAIN_FLAT)


def test_parse_raises_exception():
    """Test the exception handle in parse function."""
    with pytest.raises(ValueError):
        parse("some_data", "wrong_extension")


def test_formatter_foo_exception():
    """Test the exception handle in formatter_foo function."""
    with pytest.raises(ValueError):
        formatter_foo("wrong_format")


def get_answer(answer_path):
    """Reads the answer file."""
    return read_file(answer_path)


@pytest.mark.parametrize('filepath1, filepath2, format_name, answer', [
    (FLAT_JSON_FILE1, FLAT_JSON_FILE2, "stylish", ANSWER_STYLISH_FLAT),
    (FLAT_YAML_FILE1, FLAT_YAML_FILE2, "stylish", ANSWER_STYLISH_FLAT),
    (FLAT_YML_FILE1, FLAT_YML_FILE2, "stylish", ANSWER_STYLISH_FLAT),
    (NESTED_JSON_FILE1, NESTED_JSON_FILE2, "stylish", ANSWER_STYLISH_NESTED),
    (NESTED_YAML_FILE1, NESTED_YAML_FILE2, "stylish", ANSWER_STYLISH_NESTED),
    (FLAT_JSON_FILE1, FLAT_JSON_FILE2, "plain", ANSWER_PLAIN_FLAT),
    (FLAT_YAML_FILE1, FLAT_YAML_FILE2, "plain", ANSWER_PLAIN_FLAT),
    (FLAT_YML_FILE1, FLAT_YML_FILE2, "plain", ANSWER_PLAIN_FLAT),
    (NESTED_JSON_FILE1, NESTED_JSON_FILE2, "plain", ANSWER_PLAIN_NESTED),
    (NESTED_YAML_FILE1, NESTED_YAML_FILE2, "plain", ANSWER_PLAIN_NESTED),
    (FLAT_JSON_FILE1, FLAT_JSON_FILE2, "json", ANSWER_JSON_FLAT),
    (FLAT_YAML_FILE1, FLAT_YAML_FILE2, "json", ANSWER_JSON_FLAT),
    (FLAT_YML_FILE1, FLAT_YML_FILE2, "json", ANSWER_JSON_FLAT),
    (NESTED_JSON_FILE1, NESTED_JSON_FILE2, "json", ANSWER_JSON_NESTED),
    (NESTED_YAML_FILE1, NESTED_YAML_FILE2, "json", ANSWER_JSON_NESTED),
])
def test_generate_diff(filepath1, filepath2, format_name, answer):
    """Tests a correct work of generate_diff function."""
    answer = get_answer(answer)
    l_answer = len(answer)  # length answer
    assert generate_diff(filepath1, filepath2, format_name) == answer[:l_answer - 1]
