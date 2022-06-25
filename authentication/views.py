from django.shortcuts import render
from rest_framework.generics import GenericAPIView 
from .serializers import UserSerializer  
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
import jwt
from django.conf import settings
# Create your views here.

class RegisterView(GenericAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    def post(self, request):
        username = request.data.get('username', False)
        password = request.data.get('password', False)
        user = auth.authenticate(username=username, password=password)
        print("Auth called......................")
        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)
            data = {
                'user': serializer.data,
                'token': auth_token
            }
            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        return Response({'detail': 'Invalid Token'}, status=status.HTTP_401_UNAUTHORIZED)