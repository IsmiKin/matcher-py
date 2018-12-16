import pytest

from matcher.utils import validate_isrc, file_exists


def test_validate_isrc_valid():
    result = validate_isrc('GBAHT1200389')
    assert result is True


def test_validate_isrc_not_valid():
    result = validate_isrc('GBAHT12003890')
    assert result is not True


def test_file_exists(tmpdir):
    with pytest.raises(Exception):
        file_exists("hello.csv")

    file = tmpdir.mkdir("test").join("hello.csv")
    file.write("col1, col2")

    try:
        file_exists(file)
    except Exception:
        pytest.fail('File exists now, it should not fail')
