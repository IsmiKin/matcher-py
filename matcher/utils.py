import os
import re
import csv
import logging
from datetime import datetime


def validate_isrc(input_isrc):
    pattern = re.compile("^[A-Z]{2}-?\w{3}-?\d{2}-?\d{5}$")
    return False if pattern.match(input_isrc) is None else True


def file_exists(file_path):
    if not os.path.isfile(file_path):
        raise Exception('File does not exists')


def parse_csv(file_path):
    input_records = []
    with open(file_path, 'r') as f:
        input_records = list(csv.DictReader(f, delimiter=','))

    return input_records


def get_logger():
    FORMAT = "[%(asctime)s][%(levelname)-5.5s] %(message)s"
    logging.basicConfig(format=FORMAT)
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    return log


def get_file_metadata(file_path):
    return (os.path.basename(file_path),
            datetime.fromtimestamp(
                    os.path.getmtime(file_path)
                ).strftime('%Y-%m-%d %H:%M:%S')
            )
