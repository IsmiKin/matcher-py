import pytest
from datetime import datetime
import hashlib

from matcher.utils import validate_isrc, file_exists, get_file_metadata
from matcher.utils import get_file_hash


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


def test_file_metadata(tmpdir):
    file = tmpdir.mkdir("test").join("hello.csv")
    file.write("col1, col2")

    expected_filename = file.basename
    expected_modification_time = datetime.fromtimestamp(
        file.mtime()
        ).strftime('%Y-%m-%d %H:%M:%S')

    result_filename, result_mtime = get_file_metadata(file)

    assert expected_filename == result_filename
    assert expected_modification_time == result_mtime


def test_file_hash():
    filename = "filename"
    timestamp = "2018-12-16 21:29:22"
    file_hash_string = "{}-{}".format(
        filename, timestamp
    ).encode('utf-8')
    md5_file_hash = hashlib.md5(file_hash_string)
    expected_md5_file_hash = md5_file_hash.hexdigest()

    assert expected_md5_file_hash == get_file_hash(filename, timestamp)
