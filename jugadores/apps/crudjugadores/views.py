from django.shortcuts import render
from django.views.generic import CreateView
#CreateView crear el objeto y agregarlo a la base de datos

from apps.crudjugadores.models import Jugador
from apps.crudjugadores.models import JugadorForm

class JugadorCreate(CreateView):
    model = Jugador #modelo 
    form_class = JugadorForm #formulario que va a mostrar 
    template_name = 'crudjugadores/jugador_form.html' #la plantailla que se encarga de eso 
