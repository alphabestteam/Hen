from django.urls import path, include
from . import views


urlpatterns = [
    path('getEvent/<int:event_id>/', views.get_event, name='get_event'),
    path('getEventFile/<int:event_file_id>/', views.get_event_file, name='get_event_file'),
    path('createEvent/', views.create_event, name='create_event'),
    path('createEventFile/', views.create_event_file, name='create_event_file'),
    path('updateEvent/<int:event_id>/', views.update_event, name='update_event'),
    path('updateEventFile/<int:event_file_id>/', views.update_event_file, name='update_event_file'),
    path('getAllEvents/', views.get_all_events, name='get_all_events'),
    path('getAllEventsFile/', views.get_all_events_files, name='get_all_events_files'),
    path('deleteEvent/<int:event_file_id>/', views.delete_event, name='delete_event'),
    path('deleteEventFile/<int:event_file_id>/', views.delete_event_files, name='delete_event_files'),

    path('getEventChat/<int:chat_id>/', views.get_event_chat, name='get_chat'),
    path('createEventChat/', views.create_event_chat, name='create_chat'),
    path('updateEventChat/<int:chat_id>/', views.update_event_chat, name='update_chat'),
    path('deleteEventChat/<int:chat_id>/', views.delete_event_with_chat, name='delete_event_with_chat'),
    path('getAllEventChats/', views.get_all_event_chats, name='get_all_chats'),

    path('getMessage/<int:message_id>/', views.get_message, name='get_message'),
    path('createMessage/', views.create_message, name='create_message'),
    path('updateMessage/<int:message_id>/', views.update_message, name='update_message'),
    path('deleteMessage/<int:message_id>/', views.delete_message, name='delete_message'),
    path('getAllMessages/', views.get_all_messages, name='get_all_messages'),

    path('getChat/<int:chat_id>/', views.get_chat, name='get_chat'),
    path('createChat/', views.create_chat, name='create_chat'),
    path('updateChat/<int:chat_id>/', views.update_chat, name='update_chat'),
    path('deleteChat/<int:chat_id>/', views.delete_chat, name='delete_chat'),
    path('getAllChats/', views.get_all_chats, name='get_all_chats'),

    path('get_unread_message/<int:user_id>/<int:chat_id>/', views.get_unread_message, name='get_chat_messages'),
]