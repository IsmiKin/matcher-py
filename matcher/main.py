import fire

import data.logic
import utils

log = utils.get_logger()


def get_all_from_db():
    sound_recordings = data.logic.get_all_sound_recordings()
    for record in sound_recordings:
        log.info('PRINTING RECORD:{}'.format(record.id))


def get_candidates(input_records):
    return data.logic.infer_candidates(input_records)


def calculate_match_score__field():
    pass


def calculate_match_score():
    pass


def process_file(file_path):
    input_records = utils.parse_csv(file_path)
    records_with_candidates = get_candidates(input_records)
    for record in records_with_candidates:
        log.info('-->record {} - {}'.format(record['title'], record['artist']))
        log.info('=> candidates:')
        for candidate in record['candidates']:
            log.info('the candidate => {}'.format(candidate))
            log.info(candidate.id)
            pass


def main():
    fire.Fire()


main()
