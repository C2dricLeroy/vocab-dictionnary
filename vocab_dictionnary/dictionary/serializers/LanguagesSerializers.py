from rest_framework import serializers
from ..models import Languages

class LanguagesSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Languages
        fields = ['id', 'name', 'code', 'description', 'created_at', 'updated_at']

