from django.urls import path
from .views.entry import create_entry, get_display_name
from .views.dictionnary import create_dictionnary
urlpatterns = [
    path('create-entry/', create_entry, name='create-entry'),
    path('get-display-name/', get_display_name, name='get-display-name'),
    path('create-dictionnary/', create_dictionnary, name='create-dictionnary'),
]
