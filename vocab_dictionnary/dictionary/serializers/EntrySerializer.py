from rest_framework import serializers
from ..models import Dictionary, Entry

class EntrySerializer(serializers.ModelSerializer):
    dictionaries = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Dictionary.objects.all()
    )

    class Meta:
        model = Entry
        fields = [
            'id',
            'original_name',
            'display_name',
            'translation',
            'description',
            'dictionaries',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['display_name']

