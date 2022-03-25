from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'staking.settings')

app = Celery('staking')
app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Johannesburg')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'update_every_1hr': {
        'task': 'interests.tasks.update_interest',
        'schedule': crontab(minute='0', hour='*/1'),        
   },   
}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')