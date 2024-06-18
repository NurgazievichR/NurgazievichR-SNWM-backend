from rest_framework import serializers

from apps.user.models import UserTI

class RegisterSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(max_length = 255, write_only = True)
    class Meta:
        model = UserTI
        fields = ('email', 'password', 'password_repeat')
        extra_kwargs = {'password': {'write_only': True, 'min_length':5}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_repeat')
        user = UserTI.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)