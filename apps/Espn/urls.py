# General Imports
from django.urls import path

# Local Imports
from apps.Espn import views as espn_views

urlpatterns = [
    path('login', espn_views.login, name='user-login'),
    path('logon', espn_views.logon, name='user-logon'),
    path('logout', espn_views.logout, name='user-logout')
]