from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from dictionnary.models.entry import Entry
from dictionnary.models.dictionnary import Dictionnary
import json

@csrf_exempt
@require_POST
def create_dictionnary(request):
    try:
        data = json.loads(request.body)
        name = data['name']
        
        dictionnary = Dictionnary(name=name)
        dictionnary.save()
        
        return JsonResponse({'message': 'Dictionnary created successfully'}, status=201)
    except KeyError as e:
        return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

