from datetime import timedelta
from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
   'foo': {
       'task': 'foo',
       'schedule': timedelta(seconds=1),
   },
    'checker': {
       'task': 'checker',
       'schedule': timedelta(minutes=1),
   },
}
