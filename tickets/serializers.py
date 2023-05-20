from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Ticket, Category


class UserSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        username = serializers.CharField(max_length=255)
        password = serializers.CharField(max_length=255, style={"input_type":"password"})
        is_staff = serializers.BooleanField(default=False)

        # The function called when you create a new User object/instance
        def create(self, validated_data):
            return User.objects.create(**validated_data)
        
        # Update and return an existing `User` instance, given the validated data
        def update(self, instance, validate_data):
            instance.username = validate_data.get('username', instance.username)
            instance.password = validate_data.get('password', instance.password)
            instance.is_staff = validate_data.get('is_staff', instance.is_staff)
            instance.save()
            return instance


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'title', 'ticket_id', 'user', 'status', 'content', 'category', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')