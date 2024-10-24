from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dictionary.urls')),
    path('api/auth/', include('authentication.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('django.contrib.auth.urls')),
]
