from enum import auto
from telnetlib import STATUS
from turtle import title, update
from django.db import models
from django.contrib.admin.filters import SimpleListFilter

# Create your models here.

class CustomFilter(SimpleListFilter):
  title = "Filtro Customizado"
  parameter_name = "custom"
  def lookups(self, request, model_admin):
    return(
      ("value_01", "value 01"),
      ("value_02", "value 02"),
      ("value_03", "value 03"),
    )
  def queryset(self, request, queryset):
    if self.value() == "value_01":
      queryset = queryset.order_by("Leitor")
    elif self.value() == "value_02":
      queryset = queryset.order_by("Cadastro_Livro")
    return queryset

class Leitor(models.Model):
  STATUS = (
    (1,'Fazendo'),
    (2,'Feito'),
  )

  nome = models.CharField(max_length=250)
  sexo = models.CharField(max_length=10)
  idade = models.IntegerField()
  profissao = models.CharField(max_length=200)
  done = models.CharField(
    max_length=1,
    choices=STATUS,
  )
  created_at = models.DateTimeField(auto_now=True)
  update_at = models.DateTimeField()

class Cadastro_Livro(models.Model):
  STATUS = (
    (1,'Fazendo'),
    (2,'Feito'),
  )

  nome = models.CharField(max_length=250)
  autor = models.CharField(max_length=100)
  data_de_publicacao = models.DateTimeField()
  done = models.CharField(
    max_length=1,
    choices=STATUS,
  )
  created_at = models.DateTimeField(auto_now=True)
  update_at = models.DateTimeField()

