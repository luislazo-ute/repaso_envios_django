from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def carga_view(request):
    try:
        capacidad_kg = int(request.query_params.get("capacidad_kg", 0))
    except ValueError:
        return Response(
            {"detail": "'capacidad_kg' debe ser un entero."},
            status=status.HTTP_400_BAD_REQUEST
        )

    pesos_raw = request.query_params.get("pesos", "")
    if not pesos_raw:
        return Response(
            {"detail": "El parámetro 'pesos' es obligatorio."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        pesos = [int(p.strip()) for p in pesos_raw.split(",")]
    except ValueError:
        return Response(
            {"detail": "'pesos' debe contener enteros separados por coma."},
            status=status.HTTP_400_BAD_REQUEST
        )

    acumulado = 0
    indice    = 0
    detalles = []

    while indice < len(pesos):
        peso_actual = pesos[indice]

        if acumulado + peso_actual <= capacidad_kg:
            acumulado += peso_actual
            detalles.append(peso_actual)
            indice += 1
        else:
            break   # no cabe: detener el ciclo de inmediato

    return Response({
        "paquetes": len(detalles),
        "capacidad_restante": capacidad_kg-acumulado,
        "detalle":          detalles,
    })