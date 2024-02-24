from django.urls import path

from mails.apps import MailsConfig
from mails.views import base

app_name = MailsConfig.name

urlpatterns = [
    path('', base),
]