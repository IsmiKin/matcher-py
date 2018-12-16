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

    def __init__(
        self,
        file_hash,
        sound_record_id,
        row_number,
        artist,
        title,
        isrc,
        duration,
        score
    ):
        match_id = "{}-{}-{}".format(
            file_hash,
            row_number,
            sound_record_id
        )
        self.match_id = match_id
        self.files_processed_FK = file_hash
        self.sound_recordings_FK = sound_record_id
        self.row_number = row_number
        self.artist = artist
        self.title = title
        self.isrc = isrc
        self.duration = duration
        self.score = score
