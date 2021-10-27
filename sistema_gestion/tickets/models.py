from django.db import models
from django.db.models import Case, Value, When
from django.utils import timezone

"""
Segun el desafio:
 > ID
 > Titulo
 > Descripción
 > Estados (Abierto, Pendiente, En Proceso, Resuelto y Cerrado)
 > Fecha de Creación
"""


class Ticket(models.Model):

    OP = 1
    PD = 2
    EP = 3
    CR = 4
    CC = 5

    ESTADOS = (
        (OP, 'Abierto'),
        (PD, 'Pendiente'),
        (EP, 'En Proceso'),
        (CR, 'Resuelto'),
        (CC, 'Cerrado'),
    )

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.IntegerField(choices=ESTADOS)
    fecha_creacion = models.DateTimeField(default=timezone.now)
