from django.urls import path

from messemail.apps import MessemailConfig
from messemail.views import ClientListView, ClientCreateView, ClientUpdateView, MessageListView, MessageCreateView
app_name = MessemailConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name='edit'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
]
