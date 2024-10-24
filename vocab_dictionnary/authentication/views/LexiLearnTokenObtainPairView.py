from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import (LexiLearnTokenObtainPairSerializer)


class LexiLearnTokenObtainPairView(TokenObtainPairView):
    serializer_class = LexiLearnTokenObtainPairSerializer
