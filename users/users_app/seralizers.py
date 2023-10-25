from datetime import datetime, timezone
from rest_framework import serializers
from .models import User, Message, UserK
from dateutil.relativedelta import relativedelta

class UserKSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserK
        fields = ['name']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = User
        fields = ["name", "email", "birth_date", "user", "is_adult", "messages"]  # Include "messages" field
        read_only_fields = ["email"]

    is_adult = serializers.SerializerMethodField('get_is_adult')

    def get_is_adult(self, obj):
        now = datetime.now(timezone.utc).date()  # Convert to date object
        return obj.birth_date <= now - relativedelta(years=18)



