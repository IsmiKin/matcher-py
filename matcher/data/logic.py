import os
import hashlib
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from data.models import SoundRecording, FilesProcessed
from utils import validate_isrc, get_logger

DB_HOST = os.environ.get('DB_URL',
                         'postgresql://{0}:{1}@{2}/{3}'.format(
                            os.environ.get('DB_USERNAME'),
                            os.environ.get('DB_PASSWORD'),
                            os.environ.get('DB_HOSTNAME'),
                            os.environ.get('DB_NAME')
                            ))

engine = create_engine(DB_HOST, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

log = get_logger()


def get_all_sound_recordings():
    return session.query(SoundRecording).all()


# IDEA: if files wouldn't be big, it could be use hashing to detect
# if the file is really not being used before
def check_file_already_proccessed(filename, modification_time):
    file_hash_string = "{}-{}".format(
        filename,
        modification_time
    ).encode('utf-8')
    file_hash = hashlib.md5(file_hash_string)
    return session.query(FilesProcessed).filter_by(
        hash=file_hash.hexdigest()
    ).count() > 0


def infer_candidates(input_records):
    # TO README: It could be improve if it there will be a "cache" db with
    # only isrc and artist (and maybe title), to prevent look up at big table

    for index, record in enumerate(input_records):
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
