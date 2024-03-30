from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    'notifier-cervice',
    broker='redis://redis_service:6379/0',
    backend='redis://redis_service:6379/0',
    include=['celery_app.tasks']
)

celery_app.conf.timezone = 'UTC'

celery_app.conf.beat_schedule = {
    # 'print-hello-every-10-seconds': {
    #     'task': 'celery_app.tasks.print_hello',
    #     'schedule': timedelta(seconds=10), # 
    #     # 'schedule': crontab(minute='*'),
    # },
    'fetch_data': {
        'task': 'celery_app.tasks.fetch_data_wrapper',
        # 'schedule': timedelta(seconds=5), # 
        'schedule': crontab(minute='*/15'),
    },
}
