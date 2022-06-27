from django.contrib import admin
from .models import Leitor, Cadastro_Livro

# Register your models here.

admin.site.register(Leitor)
admin.site.register(Cadastro_Livro)