
from ..data.file_repository import get_csv_file_from_storage
from .validation import validate_process_file_endpoint
import matcher.utils as utils
import matcher.data.logic as data
import matcher.score as score


MIN_ACCEPTABLE_SCORE = 70

log = utils.get_logger()


def process_file(params):
    validate_process_file_endpoint(params)
    filename = params['filename']

    file_path = get_csv_file_from_storage(filename)

    utils.file_exists(file_path)

    filename, mod_time = utils.get_file_metadata(file_path)
    file_hash = utils.get_file_hash(filename, mod_time)

    csv_content = utils.parse_csv(file_path)
    utils.silent_remove(file_path)

    if data.logic.file_already_proccessed(file_hash):
        log.info('The file {} has been already processed')
    else:
        log.info('Start processing {}'.format(filename))
        data.create_file_processed(file_hash, filename, mod_time)
        input_records = utils.parse_csv(file_path)
        records_with_candidates = data.logic.infer_candidates(input_records)
        process_rows(file_hash, records_with_candidates)
        log.info('Finished processing {}'.format(filename))

    return csv_content


def process_rows(file_hash, records_with_candidates):
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
                data.logic.create_record_match(
                    file_hash,
                    record,
                    candidate,
                    match_score
                )
                # store
