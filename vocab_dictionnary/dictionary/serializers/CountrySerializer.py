from rest_framework import serializers
from ..models import Country
from . import LanguagesSerializers

class CountrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    languages = LanguagesSerializers(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'name', 'code', 'languages', 'latitude', 'longitude', 'created_at', 'updated_at']
