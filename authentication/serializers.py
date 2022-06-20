from dataclasses import field, fields
import email
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=5 ,write_only=True)
    email = serializers.CharField(max_length=100, min_length=5)
    first_name = serializers.CharField(max_length=50, min_length=5)
    last_name = serializers.CharField(max_length=50, min_length=5)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']
    def validate(self, attrs):
        email = User.objects.filter(email=attrs.get('email','')).exists()
        if email:
            raise serializers.ValidationError(detail='Email already in use')
        
        return super().validate(attrs) 
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
           