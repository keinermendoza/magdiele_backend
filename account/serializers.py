from .models import User 
from rest_framework import serializers

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']