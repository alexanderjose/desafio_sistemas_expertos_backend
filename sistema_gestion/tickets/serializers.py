from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Ticket
# from django.core.cache import cache


class TicketSerializer(serializers.ModelSerializer):
    estado_nombre = serializers.SerializerMethodField()

    def get_estado_nombre(self, obj):
        if obj.estado == 1:
            estado_verbose = "Abierto"
        elif obj.estado == 2:
            estado_verbose = "Pendiente"
        elif obj.estado == 3:
            estado_verbose = "En Proceso"
        elif obj.estado == 4:
            estado_verbose = "Resuelto"
        elif obj.estado == 5:
            estado_verbose = "Cerrado"
        return estado_verbose

    class Meta:
        model = Ticket
        fields = (
            'id', 'titulo', 'descripcion', 'estado', 'fecha_creacion',
            'estado_nombre'
        )


class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        # Store in cache
        # cache.set(token['username'], token, TIME_OUT)
        return token
