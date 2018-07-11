import os
from celery import Celery


# set the default Django settings module for the celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')

app = Celery('ecom', broker='redis://localhost:6379/0')

# app.result_backend = 'db+sqlite:///results.db'
app.conf.broker_url = 'redis://localhost:6379/0'

app.conf.broker_transport_options = {'visibility_timeout': 360}  # 1 hour.

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.result_backend = 'redis://localhost:6379/0'

# discover tasks.py from all the apps
app.autodiscover_tasks()



