from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegistrationSerializer


class LoginView(APIView):

    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            token = AuthToken.objects.create(user)[1]
            return Response({
                 'token' : token,
                 "first_name": user.first_name,
                 "last_name" : user.last_name,
                 "email_address" : user.email
                })
        return Response({'error': 'Invalid credential'})


class RegisterView(APIView):
    serializer_class = RegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User registered successfullty"
                }, status= status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)