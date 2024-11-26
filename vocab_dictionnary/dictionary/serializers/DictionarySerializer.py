from rest_framework import serializers
from ..serializers import EntrySerializer
from ..models import Dictionary
from random import sample

class DictionarySerializer(serializers.ModelSerializer):
    entries = serializers.SerializerMethodField()

    class Meta:
        model = Dictionary
        fields = ['id', 'name', 'source_language', 'target_language', 'entries']
        read_only_fields = ['id']

    def get_entries(self, obj):
        """Get all entries if it's a list, else get random 3"""
        request = self.context.get('request')
        if request and request.resolver_match.url_name == 'dictionary-list':
            entries = obj.entries.all()
            limited_entries = sample(list(entries), min(len(entries), 3))
            return EntrySerializer(limited_entries, many=True).data
        elif request and request.resolver_match.url_name == 'dictionary-detail':
            entries = obj.entries.all()
            return EntrySerializer(entries, many=True).data
        return None