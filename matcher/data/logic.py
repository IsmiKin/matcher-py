from sqlalchemy import or_
from utils import validate_isrc, get_logger

from data.models import (SoundRecording, FilesProcessed, SoundRecordMatch,
                         session
                         )

log = get_logger()


def get_all_sound_recordings():
    return session.query(SoundRecording).all()


# IDEA: if files wouldn't be big, it could be use hashing to detect
# if the file is really not being used before
def file_already_proccessed(file_hash):
    return session.query(FilesProcessed).filter_by(
        hash=file_hash
    ).count() > 0


# def create_record_match(filename, record, candidate, match_score):
#     match_id = "{}-{}-{}".format(
#         filename,
#         record['row_number'],
#         candidate['id']
#     )
#     new_record_match = SoundRecordMatch(
#         match_id,
#         record['row_number'],
#         record['artist'],
#         record['title'],
#         record['isrc'],
#         record['duration'],
#         match_score,
#         # sound_recordings_FK
#     )


def create_file_processed(file_hash, filename, modification_time):
    new_file_processed = FilesProcessed(file_hash, filename, modification_time)
    session.add(new_file_processed)
    session.commit()


def infer_candidates(input_records):
    # TO README: It could be improve if it there will be a "cache" db with
    # only isrc and artist (and maybe title), to prevent look up at big table

    for index, record in enumerate(input_records):
        input_records[index]['row_number'] = index
        input_records[index]['candidates'] = []
        if 'isrc' in record and validate_isrc(record['isrc']):
            candidates_by_isrc = session.query(SoundRecording).filter_by(
                                isrc=record['isrc']
                        ).first()

            input_records[index]['candidates'].append(candidates_by_isrc)

        candidates_artist_title = session.query(SoundRecording).filter(
                        or_(
                            SoundRecording.artist.ilike("%{}%".format(
                                record['artist']
                            )),
                            SoundRecording.title.ilike("%{}%".format(
                                record['title']
                            )),
                            )
                    ).all()
        input_records[index]['candidates'].extend(candidates_artist_title)
    return input_records
