import math
from random import randint
from re import template
from django.http import HttpResponse
from django.template import Context, Template, loader


def inicio(request):
    return HttpResponse("Hola, soy la nueva pagina")

def otra_vista(request):
    return HttpResponse('''
                        <h1>Alto titulo</h1>
                        ''')
    
def numero_random(request):
    numero = randint(0,100)
    return HttpResponse(numero)

def input(request, numero):
    return HttpResponse(numero)

def miPlantilla(request):
    #plantilla = open(r"C:\Users\facundo.ibarra\Desktop\miproyecto\miproyecto\Plantillas\miPlantilla.html")
    #template = Template(plantilla.read())
    
    template = loader.get_template("miPlantilla.html")
    
    nombre = 'Juan'
    apellido = 'Perez'
    
    lista_n = list(nombre)
    
    colores = ["red", "blue", "green", "yellow", "black"]
    
    color = colores[randint(0,4)]
    
    diccionario_de_datos = {
        'nombre' : nombre,
        'apellido' : apellido,
        'nombre_largo' : len(nombre),
        'lista_n' : lista_n,
        'color' : color,
    }
    
    #contect = Context(diccionario_de_datos)
    
    plantilla_preparada = template.render(diccionario_de_datos)
    
    return HttpResponse(plantilla_preparada)

