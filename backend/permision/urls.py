from django.urls import path
from .views import register, register_JKArman

urlpatterns = [
    path('register/', register, name='register'),
    path('register_JKArman/', register_JKArman, name='register_JKArman')
]
