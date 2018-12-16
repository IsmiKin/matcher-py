import fire

import data.logic
import score.logic
import utils

log = utils.get_logger()

MIN_ACCEPTABLE_SCORE = 70


def process_rows(records_with_candidates):
    for record in records_with_candidates:
        # log.info('-->record {} by  {} [{}] ({} min)'.format(
        #     record['title'],
        #     record['artist'],
        #     record['isrc'],
        #     record['duration'],
        # ))
        for candidate in record['candidates']:
            match_score = score.logic.calculate_match_score(record, candidate)
            # log.info('the candidate => {} with SCORE: {}'.format(
            #     candidate, match_score
            # ))
            if match_score > MIN_ACCEPTABLE_SCORE:
                pass
                # store


def process_file(file_path):
    utils.file_exists(file_path)
    filename, modification_time = utils.get_file_metadata(file_path)
    if data.logic.check_file_already_proccessed(filename, modification_time):
        log.info('The file {} has been already processed')
    else:
        data.logic.mark_file_as_processed(filename, modification_time)
        input_records = utils.parse_csv(file_path)
        records_with_candidates = data.logic.infer_candidates(input_records)
        process_rows(records_with_candidates)


def main():
    fire.Fire()


main()
