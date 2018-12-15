# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class FilesProcessed(Base):
    __tablename__ = 'files_processed'

    hash = Column(Integer, primary_key=True, server_default=text("nextval('files_processed_hash_seq'::regclass)"))
    filename = Column(Text, nullable=False)
    file_time_update = Column(DateTime, nullable=False)


class SoundRecording(Base):
    __tablename__ = 'sound_recordings'

    id = Column(Integer, primary_key=True, server_default=text("nextval('sound_recordings_id_seq'::regclass)"))
    artist = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    isrc = Column(Text)
    duration = Column(Integer)
