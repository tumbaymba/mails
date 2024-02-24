from django.urls import path

from mails.apps import MailsConfig
from mails.views import IndexView, contacts, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView

app_name = MailsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('create/', ClientCreateView.as_view(), name='create_client'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

]
