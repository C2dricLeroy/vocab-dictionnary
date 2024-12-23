from rest_framework import serializers
from dictionary.models import Entry


class GlobalStatisticsSerializer(serializers.Serializer):
    total_words_added = serializers.SerializerMethodField()

    def get_total_words_added(self, obj):
        return Entry.objects.count()
