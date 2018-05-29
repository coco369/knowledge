
from celery import Celery

app = Celery('first_celery_tasks', backend='redis://localhost', broker='redis://localhost')

@app.task
def add(x, y):
    return x + y
