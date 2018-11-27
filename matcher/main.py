import fire

import data.logic
import score.logic
import utils

log = utils.get_logger()

MIN_ACCEPTABLE_SCORE = 70


def process_file(file_path):
    input_records = utils.parse_csv(file_path)
    records_with_candidates = data.logic.infer_candidates(input_records)
    for record in records_with_candidates:
        log.info('-->record {} by  {} [{}] ({} min)'.format(
            record['title'],
            record['artist'],
            record['isrc'],
            record['duration'],
        ))
        for candidate in record['candidates']:
            match_score = score.logic.calculate_match_score(record, candidate)
            log.info('the candidate => {} with SCORE: {}'.format(
                candidate, match_score
            ))
            if match_score > MIN_ACCEPTABLE_SCORE:
                pass
                # store


def main():
    fire.Fire()


main()
