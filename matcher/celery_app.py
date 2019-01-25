import os
from celery import Celery
from matcher.tasks.process_file import process_file

app = Celery(
    'matcher',
    broker=os.environ.get('BROKER_URL', 'redis://localhost:6379/0'),
    backend=os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True
)


@app.task
def process_file_task(file_path):
    return process_file(file_path)
