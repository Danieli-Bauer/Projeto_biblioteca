from importlib.resources import path
from operator import index
from .import views
from django.urls import path

urlpatterns = [
    
    path('login/',views.login,name='login'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('plataforma/',views.plataforma,name='plataforma'),
    
]
