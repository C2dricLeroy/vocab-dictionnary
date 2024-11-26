from rest_framework import serializers
from .DescriptionSerializer import DescriptionSerializer
from ..models import Dictionary, Entry

class EntrySerializer(serializers.ModelSerializer):
    dictionaries = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Dictionary.objects.all()
    )
    descriptions = DescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Entry
        fields = [
            'id',
            'original_name',
            'display_name',
            'translation',
            'dictionaries',
            'descriptions',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['display_name']

