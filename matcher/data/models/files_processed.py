from sqlalchemy import Column, DateTime, Text

from .base import Base


class FilesProcessed(Base):
    __tablename__ = 'files_processed'

    hash = Column(Text,
                  primary_key=True,
                  server_default=None
                  )
    filename = Column(Text, nullable=False)
    file_time_update = Column(DateTime, nullable=False)

    def __init__(self, hash, filename, file_time_update):
        # Refactor this to smth better
        if hash is None:
            raise Exception('Hash is mandatory!')
        self.hash = hash
        self.filename = filename
        self.file_time_update = file_time_update
