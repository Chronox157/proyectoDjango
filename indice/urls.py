
from django.urls import path
from .views import inicio, miPlantilla, otra_vista, numero_random, input


urlpatterns = [
    path('inicio/', inicio),
    path('', otra_vista),
    path('random/', numero_random),
    path('input/<int:numero>', input),
    path('miPlantilla/', miPlantilla),
]
