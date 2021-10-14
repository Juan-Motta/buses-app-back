from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from apps.reservas.models import Reserva
from apps.reservas.api.serializers import ReservaListSerializer, ReservaSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def reserva_api_view(request):
    if request.method == 'GET':
        # queryset
        reservas = Reserva.objects.all()
        reservas_serializer = ReservaListSerializer(reservas, many=True)
        return Response(reservas_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        reserva_serializer = ReservaSerializer(data=request.data)
        if reserva_serializer.is_valid():
            reserva_serializer.save()
            return Response({'message': 'Reserva creada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(reserva_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def reserva_detail_api_view(request, id=None):
    # queryset
    reserva = Reserva.objects.filter(id=id).first()

    # validation
    if reserva:

        # retrieve
        if request.method == 'GET':
            reserva_serializer = ReservaListSerializer(reserva)
            return Response(reserva_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            reserva_serializer = ReservaSerializer(reserva, data=request.data)
            if reserva_serializer.is_valid():
                reserva_serializer.save()
                return Response(reserva_serializer.data, status=status.HTTP_200_OK)
            return Response(reserva_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            reserva.delete()
            return Response({'message': 'Reserva eliminada correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado una reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
