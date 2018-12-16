from sqlalchemy import Column, DateTime, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class FilesProcessed(Base):
    __tablename__ = 'files_processed'

    hash = Column(Text,
                  primary_key=True,
                  server_default=(
                      text("nextval('files_processed_hash_seq'::regclass)")
                     )
                  )
    filename = Column(Text, nullable=False)
    file_time_update = Column(DateTime, nullable=False)
