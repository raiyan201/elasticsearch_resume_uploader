import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','resume_uploader.settings')
app=Celery('resume_uploader')
app.config_from_object('django.conf:settings', namespace="CELERY")


app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
