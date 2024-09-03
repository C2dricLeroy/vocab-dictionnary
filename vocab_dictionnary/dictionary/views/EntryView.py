from django.shortcuts import get_object_or_404
from ..models import Dictionary, Entry
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import EntrySerializer


class CreateEntryView(APIView):
    def post(self, request):
        data = request.data
        try:
            name = data['name']
            traduction = data['traduction']
            dictionary_id = data['dictionnary_id']
            dictionary = get_object_or_404(Dictionary, id=dictionary_id)
            entry = Entry(
                name=name,
                traduction=traduction,
                dictionnary=dictionary
            )
            entry.save()
            return Response(
                {'message': 'Entry created successfully'},
                status=status.HTTP_201_CREATED
            )
        except KeyError as e:
            return Response(
                {'error': f"Missing key: {e.args[0]}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetEntry(APIView):
    def get(self, request):
        entry_id = request.GET.get('id')

        if not entry_id:
            return Response(
                {"error": "Missing 'id' parameter"},
                status=status.HTTP_400_BAD_REQUEST
            )
        entry = get_object_or_404(Entry, id=entry_id)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)


class UpdateEntry(APIView):
    def post(self, request):
        entry_data = request.data
        pass