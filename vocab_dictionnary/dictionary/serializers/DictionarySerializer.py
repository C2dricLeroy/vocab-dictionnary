from rest_framework import serializers
from ..models import Dictionary, Languages
from django.shortcuts import get_object_or_404


class DictionarySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Dictionary
        fields = ['id', 'name', 'source_language', 'target_language']
