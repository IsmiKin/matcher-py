from matcher.utils import validate_isrc


def test_validate_isrc_valid():
    result = validate_isrc('GBAHT1200389')
    assert result is True


def test_validate_isrc_not_valid():
    result = validate_isrc('GBAHT12003890')
    assert result is not True
