import re
import csv

def validate_isrc(input_isrc):
    pattern = re.compile("^[A-Z]{2}-?\w{3}-?\d{2}-?\d{5}$")
    return False if pattern.match(input_isrc) is None else True


def parse_csv(file_path):
    input_records = []
    with open(file_path, 'r') as f:
        input_records = list(csv.DictReader(f, delimiter=','))

    return input_records
