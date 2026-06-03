from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def costos_view(request):
    paquetes = request.data.get("paquetes", [])

    if not isinstance(paquetes, list) or len(paquetes) == 0:
        return Response(
            {"detail": "El campo 'paquetes' debe ser una lista no vacía."},
            status=status.HTTP_400_BAD_REQUEST
        )

    total_cobro = 0
    total_paquetes=0
    detalle     = []

    for paquete in paquetes:
        destinatario      = paquete.get("destinatario", "")
        peso_kg       = float(paquete.get("peso_kg", 0))
        tipo = int(paquete.get("tipo", 0))#1 normal, 2 fragil, 3 refrigerado

        # Determinar porcentaje de recargo según días de atraso
        if tipo == 1:
            costo = 3
        elif tipo == 2:
            costo = 5
        elif tipo == 3:
            costo = 8
        
        if peso_kg <= 5:
            recargo= 0
        elif peso_kg <= 10:
            recargo = 2
        else:
            recargo = 4
            
        costo_total = round(costo + recargo, 2)
        total_cobro += costo_total
        total_paquetes+=1

        detalle.append({
            "destinatario": destinatario,
            "costo_base": costo,
            "costo_total": costo_total,
        })

    return Response({
        "total_paquetes": total_paquetes,
        "total_cobro":  total_cobro,
        "detalle":      detalle,
    })