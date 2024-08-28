from django.urls import path
from . import create_entry, get_display_name
from . import create_dictionnary, get_dictionary_by_id


urlpatterns = [
    path('create-entry/', create_entry, name='create-entry'),
    path('get-display-name/', get_display_name, name='get-display-name'),
    path('create-dictionnary/', create_dictionnary, name='create-dictionnary'),
    path('get-dictionary-by-id', get_dictionary_by_id, name='get-dictionary-by-id' )
]
