from django.urls import path

from mails.apps import MailsConfig
from mails.views import IndexView, contacts, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MailsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/view/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/view/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

]
