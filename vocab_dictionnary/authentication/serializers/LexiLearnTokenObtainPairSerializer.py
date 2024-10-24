from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import exceptions


class LexiLearnTokenObtainPairSerializer(TokenObtainPairSerializer):

    default_error_messages = {
        "invalid_credentials": ("Wrong password or username.")
    }

    def validate(self, attrs):
        username_or_email = attrs.get('username')
        password = attrs.get('password')

        user = None

        try:
            user = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed(self.error_messages["invalid_credentials"])

        if user and not user.check_password(password):
            raise exceptions.AuthenticationFailed(self.error_messages["invalid_credentials"])

        attrs['username'] = user.username

        return super().validate(attrs)
