from sqlalchemy import Column, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SoundRecording(Base):
    __tablename__ = 'sound_recordings'

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('sound_recordings_id_seq'::regclass)")
    )
    artist = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    isrc = Column(Text)
    duration = Column(Integer)

    def __repr__(self):
            return "{} by {} ({} min) [{}]".format(
                self.title, self.artist, self.duration, self.isrc
                )
