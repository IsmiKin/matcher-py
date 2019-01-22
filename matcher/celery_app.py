import os
from celery import Celery

app = Celery(
    'matcher',
    broker=os.environ.get('BROKER_URL', 'redis://localhost:6379/0'),
    backend=os.environ.get('BACKEND_RESULT_URL', 'redis://localhost:6379/0')
)


@app.task
def add(x, y):
    return x + y
