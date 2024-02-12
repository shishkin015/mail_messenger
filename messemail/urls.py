from django.urls import path

from messemail.apps import MessemailConfig
from messemail.views import MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, \
    MailingSettingsUpdateView, MailingLogsListView, MessageCreateView, MessageListView, MessageDetailView, \
    MessageUpdateView, MessageDeleteView

app_name = MessemailConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('add/', MailingCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='update'),
    path('<int:pk>/', MailingDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
    path('settings/<int:pk>', MailingSettingsUpdateView.as_view(), name='detail_settings'),
    path('logs/', MailingLogsListView.as_view(), name='logs'),

    path('mail_create/', MessageCreateView.as_view(), name='mail_create'),
    path('mail_list/', MessageListView.as_view(), name='mail_list'),
    path('mail/<int:pk>/', MessageDetailView.as_view(), name='mail_detail'),
    path('mail/update/<int:pk>', MessageUpdateView.as_view(), name='mail_update'),
    path('mail/delete/<int:pk>', MessageDeleteView.as_view(), name='mail_delete'),
]