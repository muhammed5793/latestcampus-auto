import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_campus.settings')

app = Celery('smart_campus')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
