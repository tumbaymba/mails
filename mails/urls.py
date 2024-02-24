from django.urls import path

from mails.apps import MailsConfig
from mails.views import IndexView, contacts

app_name = MailsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),

]
