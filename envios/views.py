from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Ruta, Paquete
from .serializers import RutaSerializer, PaqueteSerializer
from .permissions import IsAdminOrReadOnly

class RutaViewSet(viewsets.ModelViewSet):
    queryset           = Ruta.objects.all().order_by("id")
    serializer_class   = RutaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields      = ["nombre"]
    ordering_fields    = ["id", "nombre", "codigo"]

class PaqueteViewSet(viewsets.ModelViewSet):
    queryset           = Paquete.objects.select_related("ruta").all().order_by("destinatario")
    serializer_class   = PaqueteSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ["ruta"]
    search_fields      = ["destinatario", "codigo"]
    ordering_fields    = ["id", "destinatario", "codigo"]

    def get_permissions(self):
        # GET /api/paquetes/ es público sin token
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()