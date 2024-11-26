from rest_framework import serializers
from ..models import Description

class DescriptionSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Description
        fields = ['id', 'entry', 'text', 'created_by', 'created_at']
