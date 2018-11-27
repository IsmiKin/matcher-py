import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.models.sound_recording import SoundRecording

DB_HOST = os.environ.get('DB_URL',
                         'postgresql://{0}:{1}@{2}/{3}'.format(
                            os.environ.get('DB_USERNAME'),
                            os.environ.get('DB_PASSWORD'),
                            os.environ.get('DB_HOSTNAME'),
                            os.environ.get('DB_NAME')
                            ))

engine = create_engine(DB_HOST, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def get_all_sound_recordings():
    return session.query(SoundRecording).all()
