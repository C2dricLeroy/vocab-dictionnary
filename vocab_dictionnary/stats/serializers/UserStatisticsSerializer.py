from rest_framework import serializers
from django.contrib.auth.models import User
from dictionary.models import Entry


class UserStatisticsSerializer(serializers.ModelSerializer):
    total_dictionaries = serializers.SerializerMethodField()
    total_entries = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'total_dictionaries', 'total_entries']

    def get_total_dictionaries(self, obj):
        return obj.dictionaries.count()

    def get_total_entries(self, obj):
        return Entry.objects.filter(dictionaries__user=obj).count()
