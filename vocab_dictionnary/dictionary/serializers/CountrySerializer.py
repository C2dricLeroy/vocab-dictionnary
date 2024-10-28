from rest_framework import serializers
from ..models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'code', 'latitude', 'longitude', 'created_at', 'updated_at']
