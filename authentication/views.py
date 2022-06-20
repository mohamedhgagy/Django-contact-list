from django.shortcuts import render
from rest_framework.generics import GenericAPIView 
from .serializers import UserSerializer  
from rest_framework.response import Response
from rest_framework import status
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
        user = seriali