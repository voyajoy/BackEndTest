from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend',
        broker='redis://redis:6379/0',
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-every-hour': {
        'task': 'backend.api.tasks.fetch_commits',
        'schedule': 3600.0,
    }
}
