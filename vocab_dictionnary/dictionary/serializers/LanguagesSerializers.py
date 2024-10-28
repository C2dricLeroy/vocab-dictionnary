from rest_framework import serializers
from ..models import Languages

class LanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ['name', 'description', 'created_at', 'updated_at']
