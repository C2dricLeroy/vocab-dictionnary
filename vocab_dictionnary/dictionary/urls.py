from django.urls import path
from .views.CreateDictionaryView import CreateDictionaryView

urlpatterns = [
    path('create-dictionary/', CreateDictionaryView.as_view(), 
         name='create-dictionary'),
   ]
