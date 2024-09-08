from rest_framework import serializers
from ..models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ['name', 'source_language_id', 'target_language_id']

    def validate_data(self):
        pass
