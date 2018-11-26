import re


def validate_isrc(input_isrc):
    pattern = re.compile("^[A-Z]{2}-?\w{3}-?\d{2}-?\d{5}$")
    return False if pattern.match(input_isrc) is None else True
