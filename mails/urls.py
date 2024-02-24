from django.urls import path

from mails.apps import MailsConfig
from mails.views import IndexView, contacts,ClientListView

app_name = MailsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('client/', ClientListView.as_view(), name='client_list'),

]
