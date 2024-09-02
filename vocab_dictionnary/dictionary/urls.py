from django.urls import path
from .views.dictionnary import get_dictionary_by_id, create_dictionary
from .views.entry import create_entry, get_display_name_by_id

urlpatterns = [
    path('create-entry/', create_entry, name='create-entry'),
    path('get-display-name/', get_display_name_by_id, name='get-display-name'),
    path('create-dictionary/', create_dictionary, name='create-dictionary'),
    path('get-dictionary-by-id', get_dictionary_by_id, name='get-dictionary-by-id' )
]
