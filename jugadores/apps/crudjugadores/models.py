from django.db import models

class Deporte(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)


class Jugador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=50)
    deporte = models.ForeignKey(Deporte, null=True,blank=True,on_delete=models.CASCADE)




