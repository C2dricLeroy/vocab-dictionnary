from django.urls import path
from .views.SignUp import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]