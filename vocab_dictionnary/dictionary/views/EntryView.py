
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


    def get_entry_by_name(self):
        entry_name = self.request.data.GET.get('name')

        if not entry_name:
            return HttpResponseBadRequest(JsonResponse({'error': 'Name parameter is missing'}, status=400))

        try:
            entry = Entry.objects.get(name=entry_name)
            return JsonResponse({'entry': entry.to_dict()})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Entry not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_display_name_by_id(self):
        user_id = self.request.GET.get('id')

        if not user_id:
            return HttpResponseBadRequest(JsonResponse({'error': 'ID parameter is missing'}, status=400))

        try:
            entry = Entry.objects.get(id=user_id)
            display_name = entry.get_display_name()

            return JsonResponse({'display_name': display_name})

        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Entry not found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
