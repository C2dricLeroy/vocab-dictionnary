from rest_framework import serializers
from ..models import Dictionnary, Languages, Entry

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionnary
        fields = ['name', 'source_language', 'target_language']