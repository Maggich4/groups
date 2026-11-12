from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .views import (
    register,
    register_JKArman,
    register_choice,
    response_perm,
    CustomLoginView,
    profile
)

urlpatterns = [
    path(
        'change_password/', PasswordChangeView.as_view(
            template_name='permision/change.html',
            success_url=reverse_lazy('profile')
        ), 
        name='change_password'
    ),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('response_perm/', response_perm, name='response_perm'),
    path('register_choice/', register_choice, name='register_choice'),
    path('register_JKArman/', register_JKArman, name='register_JKArman'),
]
