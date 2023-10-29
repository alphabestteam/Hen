from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import regularEvent,EventWithFiles,eventWithChat,message,chat,User
from .serializers import RegularEventSerializer,EventWithFilesSerializer,EventWithChatSerializer,MessageSerializer,ChatSerializer

@api_view(['DELETE'])
def delete_event(request, event_id):
    event = get_object_or_404(regularEvent, id=event_id)
    event.delete()
    return Response({"message": "Event deleted successfully"})
@api_view(['DELETE'])
def delete_event_files(request, event_files_id):
    event = get_object_or_404(EventWithFiles, id=event_files_id)
    event.delete()
    return Response({"message": "Event deleted successfully"})

@api_view(['GET'])
def get_all_events(request):
    events = regularEvent.objects.filter(in_archives=False)
    serializer = RegularEventSerializer(events, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_all_events_files(request):
    events = EventWithFiles.objects.filter(in_archives=False)
    serializer = EventWithFilesSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_event(request, event_id):
    event = get_object_or_404(regularEvent, id=event_id)
    serializer = RegularEventSerializer(event)
    return Response(serializer.data)
@api_view(['GET'])
def get_event_file(request, event_file_id):
    event = get_object_or_404(EventWithFiles, id=event_file_id)
    serializer = EventWithFilesSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
def create_event(request):
    data = request.data
    if 'users_names' in data and not isinstance(data['users_names'], list):
        data['users_names'] = [data['users_names']]
    serializer = RegularEventSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
@api_view(['POST'])
def create_event_file(request):
    data = request.data
    if 'users_names' in data and not isinstance(data['users_names'], list):
        data['users_names'] = [data['users_names']]
    serializer = EventWithFilesSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_event(request, event_id):
    event = get_object_or_404(regularEvent, id=event_id)
    serializer = RegularEventSerializer(event, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
@api_view(['PUT'])
def update_event_file(request, event_file_id):
    event = get_object_or_404(EventWithFiles, id=event_file_id)
    serializer = EventWithFilesSerializer(event, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

@api_view(['DELETE'])
def delete_event_with_chat(request, chat_id):
    chat = get_object_or_404(eventWithChat, id=chat_id)
    chat.delete()
    return Response({"message": "Chat deleted successfully"})

@api_view(['DELETE'])
def delete_message(request, message_id):
    message = get_object_or_404(message, id=message_id)
    message.delete()
    return Response({"message": "Message deleted successfully"})

@api_view(['GET'])
def get_all_event_chats(request):
    chats = eventWithChat.objects.all()
    serializer = EventWithChatSerializer(chats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_event_chat(request, chat_id):
    chat = get_object_or_404(eventWithChat, id=chat_id)
    serializer = EventWithChatSerializer(chat)
    return Response(serializer.data)

@api_view(['POST'])
def create_event_chat(request):
    serializer = EventWithChatSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_event_chat(request, chat_id):
    chat = get_object_or_404(eventWithChat, id=chat_id)
    serializer = EventWithChatSerializer(chat, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def get_all_messages(request):
    messages = message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_message(request, message_id):
    message = get_object_or_404(message, id=message_id)
    serializer = MessageSerializer(message)
    return Response(serializer.data)

@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_message(request, message_id):
    message = get_object_or_404(message, id=message_id)
    serializer = MessageSerializer(message, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)



@api_view(['GET'])
def get_all_chats(request):
    chats = chat.objects.all()
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_chat(request, chat_id):
    chat_instance = get_object_or_404(chat, id=chat_id)
    serializer = ChatSerializer(chat_instance)
    return Response(serializer.data)

@api_view(['POST'])
def create_chat(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_chat(request, chat_id):
    chat_instance = get_object_or_404(chat, id=chat_id)
    serializer = ChatSerializer(chat_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_chat(request, chat_id):
    chat_instance = get_object_or_404(chat, id=chat_id)
    chat_instance.delete()
    return Response()

@api_view(['GET'])
def get_unread_message(request, user_id, chat_id):
    user = get_object_or_404(User, id=user_id)
    chat = get_object_or_404(eventWithChat, id=chat_id)
    if user in chat.users_names.all():
        messages = message.objects.filter(chat=chat.chat)
        message_texts = [msg.text for msg in messages]
        return Response({'messages': message_texts})
    return Response()
