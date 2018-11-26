import logging
import csv
import fire

import data.logic

FORMAT = "[%(asctime)s][%(levelname)-5.5s] %(message)s"
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)


def get_all_from_db():
    sound_recordings = data.logic.get_all_sound_recordings()
    for record in sound_recordings:
        log.info('PRINTING RECORD:{}'.format(record.id))


def get_candidates(input_records):
    return data.logic.infer_candidates(input_records)


def parse_csv(file_path):
    input_records = []
    with open(file_path, 'r') as f:
        input_records = list(csv.DictReader(f, delimiter=','))

    return input_records


def process_file(file_path):
    input_records = parse_csv(file_path)
    records_with_candidates = get_candidates(input_records)
    for record in records_with_candidates:
        log.info('-->record {} - {}'.format(record['title'], record['artist']))
        log.info('=> candidates:')
        for candidate in record['candidates']:
            log.info('the candidate => {}'.format(candidate))
            log.info(candidate)
            pass


def main():
    fire.Fire()


main()
