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
        print(validated_data)
        # **validated_data means conevrt dict to variables ex: dic = {'id':1, 'name': 'mohamed'} ===> **dic is being(id=1, name='mohamed')
        return User.objects.create_user(**validated_data)
           