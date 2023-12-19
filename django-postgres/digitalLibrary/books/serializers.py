from rest_framework import serializers
from .models import borrowBook ,sellBook

class borrowBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = borrowBook
        fields = '__all__'

class sellBookSerializers(serializers.ModelSerializer):
    class Meta(borrowBookSerializers.Meta):
        model = sellBook
        fields = ('price') + borrowBookSerializers.Meta.fields