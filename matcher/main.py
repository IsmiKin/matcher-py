import fire
from fuzzywuzzy import fuzz

import data.logic
import utils

log = utils.get_logger()

MIN_ACCEPTABLE_SCORE = 70

SCORE_METADA_SOUND_RECORDING = [
    {
        'column_name': 'isrc',
        'type_match': fuzz.ratio,
        'min_acceptable': 100,
        'final_score_percent': 1,
        'optional': True
    },
    {
        'column_name': 'title',
        'type_match': fuzz.token_sort_ratio,
        'min_acceptable': 60,
        'final_score_percent': 0.60,
        'optional': False
    },
    {
        'column_name': 'artist',
        'type_match': fuzz.token_set_ratio,
        'min_acceptable': 50,
        'final_score_percent': 0.30,
        'optional': False
    },
    #duration is number, so it will be ignore by now
    # {
    #     'column_name': 'duration',
    #     'type_match': 'duration',
    #     'min_acceptable': 50,
    #     'final_score_percent': 0.10,
    #     'optional': True
    # },
]


def get_all_from_db():
    sound_recordings = data.logic.get_all_sound_recordings()
    for record in sound_recordings:
        log.info('PRINTING RECORD:{}'.format(record.id))


def get_candidates(input_records):
    return data.logic.infer_candidates(input_records)


# def match_duration(input_record, db_record):
#     diff = abs(input_record - db_record)
#     if diff > 10:
#         return 0.00
#     elif diff == 0:
#         return 100
#     else:
#

def match_score_field(field_rules, input_record, db_record):
    # if field_rules['type_match'] == 'duration':
    #     ratio = match_duration(input_record, db_record)
    # else:
    ratio = field_rules['type_match'](input_record, db_record)
    # log.info('input_record: {} --- db record {} => ratio: {}'.format(input_record, db_record, ratio))
    return ratio


# A simpler version could be using fuzzy.process for each field, but it would
# lose precission
def calculate_match_score(input_record, db_record):
    final_score = 0.00
    # field_scores = {}
    if db_record is not None:
        for field_score_rules in SCORE_METADA_SOUND_RECORDING:
            field_score = match_score_field(
                field_score_rules,
                input_record[field_score_rules['column_name']],
                getattr(db_record, field_score_rules['column_name'])
                )
            field_score_percent = field_score * field_score_rules['final_score_percent']
            if field_score_percent == 100:
                return 100
            elif field_score < field_score_rules['min_acceptable']:
                if not field_score_rules['optional']:
                    return 0.00
                pass
            else:
                final_score += field_score_percent

    return final_score


def process_file(file_path):
    input_records = utils.parse_csv(file_path)
    records_with_candidates = get_candidates(input_records)
    for record in records_with_candidates:
        log.info('-->record {} by  {} [{}] ({} min)'.format(
            record['title'],
            record['artist'],
            record['isrc'],
            record['duration'],
        ))
        # log.info('=> candidates:')
        for candidate in record['candidates']:
            # log.info(candidate.id)
            match_score = calculate_match_score(record, candidate)
            log.info('the candidate => {} with SCORE: {}'.format(candidate, match_score))
            if match_score > MIN_ACCEPTABLE_SCORE:
                pass
                # store


def main():
    fire.Fire()


main()
