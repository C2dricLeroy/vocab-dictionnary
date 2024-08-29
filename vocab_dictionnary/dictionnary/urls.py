from django.urls import path
from dictionnary.views.dictionnary import create_dictionary
from dictionnary.models.dictionnary import Dictionnary
from .views.dictionnary import get_dictionary_by_id, create_dictionary
from .views.entry import create_entry, get_display_name_by_id

urlpatterns = [
    path('create-entry/', create_entry, name='create-entry'),
    path('get-display-name/', get_display_name_by_id, name='get-display-name'),
    path('create-dictionnary/', create_dictionary, name='create-dictionnary'),
    path('get-dictionary-by-id', get_dictionary_by_id, name='get-dictionary-by-id' )
]
