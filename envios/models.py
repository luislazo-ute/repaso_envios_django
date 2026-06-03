from django.db import models


class Ruta(models.Model):
    codigo = models.CharField(max_length=120, unique=True)
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    ruta        = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name="paquetes")
    codigo      = models.CharField(max_length=180)
    destinatario      = models.CharField(max_length=20, unique=True)
    peso = models.DecimalField(
        max_digits=10,  # total de dígitos
        decimal_places=2,  # decimales
        default=0
    )
    tipo      = models.BooleanField(default=True)
    estado   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} ({self.destinatario})"