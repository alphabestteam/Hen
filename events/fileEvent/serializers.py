from rest_framework import serializers
from .models import regularEvent ,EventWithFiles ,eventWithChat, message,User,chat

class RegularEventSerializer(serializers.ModelSerializer):
    users_names = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = regularEvent
        fields = '__all__'
    
class EventWithFilesSerializer(serializers.ModelSerializer):
    users_names = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = EventWithFiles
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'

class EventWithChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = eventWithChat
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chat
        fields = '__all__'

    