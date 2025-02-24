from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken

class LoginView(APIView):

    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            token = AuthToken.objects.create(user)[1]
            return Response({
                 'token' : token
                })
        return Response({'error': 'Invalid credential'})