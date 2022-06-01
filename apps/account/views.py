from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .models import CustomUser
from apps.account.serializers import CustomAuthTokenSerializer, RegisterSerializer
from .services.utils import send_activate_code


class LoginView(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer


class RegisterView(APIView):

    def post(self, request):
        data = request.POST
        serializer = RegisterSerializer(data=data, many=False)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user = serializer.save()
            send_activate_code(user.activate_code, user.email)
        return Response(serializer.data)


class ActivateView(APIView):

    def get(self, request, activate_code):
        user = get_object_or_404(CustomUser, activate_code=activate_code)
        user.is_active = True
        user.save()
        return Response({'message': 'all okay, your acc is activated now'})


class LogoutView(APIView):

    def get(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response(status=status.HTTP_401_UNAUTHORIZED)
