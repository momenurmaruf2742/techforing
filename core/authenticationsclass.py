from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt

class BearerAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get('Authorization', None)
        if not auth:
            return None
        
        try:
            prefix, token = auth.split(' ')
            if prefix != 'Bearer':
                return None
            
            payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            return (user, token)
        except (ValueError, jwt.ExpiredSignatureError, jwt.DecodeError):
            raise AuthenticationFailed('Invalid token')