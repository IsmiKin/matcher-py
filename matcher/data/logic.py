import os
import logging
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from data.models.sound_recording import SoundRecording
from utils import validate_isrc

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


def get_all_sound_recordings():
    return session.query(SoundRecording).all()


def infer_candidates(input_records):
    # TO README: It could be improve if it there will be a "cache" db with
    # only isrc and artist (and maybe title), to prevent look up at big table

    for index, record in enumerate(input_records):
        input_records[index]['candidates'] = []
        if 'isrc' in record and validate_isrc(record['isrc']):
            candidates_by_isrc = session.query(SoundRecording).filter(
                                SoundRecording.isrc == record['isrc']
                        ).first()

            input_records[index]['candidates'].append(candidates_by_isrc)

        candidates_by_artist_title = session.query(SoundRecording).filter(
                        or_(
                            SoundRecording.artist.ilike("%{}%".format(
                                record['artist']
                            )),
                            SoundRecording.title.ilike("%{}%".format(
                                record['title']
                            )),
                            )
                    ).all()
        input_records[index]['candidates'].extend(candidates_by_artist_title)
    return input_records
