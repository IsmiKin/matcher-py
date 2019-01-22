from sqlalchemy import Column, Integer, Text, text

from .base import Base


class SoundRecording(Base):
    __tablename__ = 'sound_recordings'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    artist = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    isrc = Column(Text)
    duration = Column(Integer)

    def __repr__(self):
            return "{} by {} ({} min) [{}]".format(
                self.title, self.artist, self.duration, self.isrc
                )
