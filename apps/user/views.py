from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from apps.user.serialziers import RegisterSerializer, LoginSerializer
from apps.user.permissions import IsNotAuthenticated

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (IsNotAuthenticated,)

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
    permission_classes = (IsNotAuthenticated,)

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
        

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id = request.user.id)
        for token in tokens:
            BlacklistedToken.objects.get_or_create(token=token)

        return Response(
            data={'Сообщение': 'Вы вышли со всех аккаунтов'},
            status=status.HTTP_205_RESET_CONTENT)