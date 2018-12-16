from .files_processed import FilesProcessed
from .sound_recording import SoundRecording
from .sound_record_match import SoundRecordMatch

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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


__all__ = ['FilesProcessed', 'SoundRecording', 'SoundRecordMatch']
