
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from ..models import Dictionary, Entry
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import EntrySerializer


class CreateEntryView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data['name']
            traduction = data['traduction']
            dictionary_id = data['dictionnary_id']
            dictionary = Dictionary.objects.get(id=dictionary_id)
            entry = Entry(
                name=name, traduction=traduction, dictionnary=dictionary
                )
            entry.save()

            return JsonResponse(
                {'message': 'Entry created successfully'}, status=201
                )
        except Dictionary.DoesNotExist:
            return JsonResponse({'error': 'Dictionnary not found'}, status=404)
        except KeyError as e:
            return JsonResponse(
                {'error': f'Missing key: {e.args[0]}'}, status=400
                )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class GetEntry(APIView):
    def get(self, request):
        entry_id = request.GET.get('id')

        if not entry_id:
            return Response({"error": "Missing 'id' parameter"}, status=400)

        entry = get_object_or_404(Entry, id=entry_id)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)


class UpdateEntry(APIView):
    def post(self, request):
        entry_data = json.loads(request.body)
        pass
