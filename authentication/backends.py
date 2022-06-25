from rest_framework import authentication, exceptions
import jwt
from django.conf import settings
from django.contrib.auth.models import User

class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        print('AUTH DATA: ',auth_data.decode('utf-8'))
        prefix, token = auth_data.decode('utf-8').split(' ')
        print("THE TOKEN :",jwt.decode(token, settings.JWT_SECRET_KEY, algorithms="HS256"))
        try:
            print("THE TOKEN :",jwt.decode(token, settings.JWT_SECRET_KEY))
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            print("PAY",payload)
            user = User.objects.get(username=payload.get('username'))
            return (user, token)
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Your token is expired')
        return super().authenticate(request)