from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from dictionnary.models import Dictionary, Languages
import json


@csrf_exempt
@require_POST
def create_dictionary(request):
    try:
        data = json.loads(request.body)
        name = data['name']
        source_language_id = data['source_language_id']
        target_language_id = data['target_language_id']

        source_language = get_object_or_404(Languages, id=source_language_id)
        target_language = get_object_or_404(Languages, id=target_language_id)

        dictionary = Dictionary.objects.create(
            name=name,
            source_language=source_language,
            target_language=target_language
        )

        return JsonResponse({'message': 'Dictionary created successfully'}, status=201)

    except KeyError as e:
        return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
