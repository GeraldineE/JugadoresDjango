from django.contrib import admin 
from django.conf.urls import url 
from apps.crudjugadores.views import JugadorCreate

urlpatterns = [
    url('nuevo/', JugadorCreate.as_view(), namespace= 'jugador_crear')),
]