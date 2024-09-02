import random

import django.db
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ..models import Dictionnary, Entry
import json


@csrf_exempt
@require_POST
def create_entry(request):
    try:
        data = json.loads(request.body)
        name = data['name']
        traduction = data['traduction']
        dictionnary_id = data['dictionnary_id']
        dictionnary = Dictionnary.objects.get(id=dictionnary_id)
        entry = Entry(name=name, traduction=traduction, dictionnary=dictionnary)
        entry.save()
        
        return JsonResponse({'message': 'Entry created successfully'}, status=201)
    except Dictionnary.DoesNotExist:
        return JsonResponse({'error': 'Dictionnary not found'}, status=404)
    except KeyError as e:
        return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_entry_by_id(request):
    pass

def get_entry_by_name(request):
    entry_name = request.GET.get('name')

    if not entry_name:
        return HttpResponseBadRequest(JsonResponse({'error': 'Name parameter is missing'}, status=400))

    try:
        entry = Entry.objects.get(name=entry_name)
        return JsonResponse({'entry': entry.to_dict()})
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Entry not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_display_name_by_id(request):
    user_id = request.GET.get('id')

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
