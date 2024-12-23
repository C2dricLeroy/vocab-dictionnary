from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers import GlobalStatisticsSerializer


class GlobalStatisticsViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path='global')
    def global_statistics(self, request):
        serializer = GlobalStatisticsSerializer({})
        return Response(serializer.data)
