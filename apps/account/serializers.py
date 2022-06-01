from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import CustomUser

 
class CustomAuthTokenSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(
        write_only=True #POST only
    )
    token = serializers.CharField(
        read_only=True #GET
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class RegisterSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password_confirm')

    def validate(self, attrs:dict):

        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("password and password_confirm are not equal")
        
        if len(password) < 8 or len(password_confirm) < 8:
            raise serializers.ValidationError("password or password_confirm < 8 characters")


        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
