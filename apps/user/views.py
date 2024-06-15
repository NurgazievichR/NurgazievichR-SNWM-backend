from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from apps.user.serialziers import RegisterSerializer, LoginSerializer

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access': str(refresh.access_token),
        })

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = authenticate(request, **serializer.validated_data)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'Детали': 'Неверные данные', 'status' : status.HTTP_401_UNAUTHORIZED })