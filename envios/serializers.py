from rest_framework import serializers
from .models import Ruta, Paquete

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        
        fields = ["id", "codigo", "nombre", "total_paquetes"]
        def get_total_paquetes(self, obj):
            return obj.paquetes.count(activo=True).count()

class PaqueteSerializer(serializers.ModelSerializer):
    ruta_nombre = serializers.CharField(source="ruta.nombre", read_only=True)

    class Meta:
        model = Paquete
        fields = ["id", "ruta", "ruta_nombre", "codigo", "destinatario", "peso", "tipo", "estado"]


    class Meta:
        model  = Paquete
        fields = ["id", "ruta","ruta_nombre", "codigo", "destinatario", "peso", "tipo", "estado"]