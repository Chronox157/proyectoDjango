from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from clase.models import Curso


# Create your views here.

def nuevo_curso(request):
    nuevo_curso = Curso(nombre="Curso Hola", camada="ds43")
    nuevo_curso.save()
    
    
    return HttpResponse(f"Se creó nuevo curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")