from django.http import JsonResponse # type: ignore
# from api.models import User
from rest_framework.views import APIView #type: ignore

from google.oauth2 import id_token
from google.auth.transport import requests

# from api.support.session_holder import SessionHolder

import sys, json, uuid, os

class GoogleLogin(APIView):
    def post(self, request):

        ID = os.environ.get("VITE_GOOGLE_ID")
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        token = body_data.get('token', None)

        if not token: return JsonResponse({'error': 'bad request'}, status=400)

        try:
            decoded_token = id_token.verify_oauth2_token(token, requests.Request(), ID)
        except ValueError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
