# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from .base import Base


class SoundRecordMatch(Base):
    __tablename__ = 'sound_record_match'

    match_id = Column(Text, primary_key=True)
    row_number = Column(Integer, nullable=False)
    artist = Column(Text)
    title = Column(Text)
    isrc = Column(Text)
    duration = Column(Integer)
    score = Column(Integer, nullable=False)
    files_processed_FK = Column(
        ForeignKey('files_processed.hash'),
        nullable=False
    )
    sound_recordings_FK = Column(
        ForeignKey('sound_recordings.id'),
        nullable=False
    )

    files_processed = relationship('FilesProcessed')
    sound_recording = relationship('SoundRecording')
