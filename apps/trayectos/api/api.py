from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.trayectos.models import Trayecto
from apps.trayectos.api.serializers import TrayectoListSerializer, TrayectoSerializer


@api_view(['GET', 'POST'])
def trayecto_api_view(request):
    if request.method == 'GET':
        # queryset
        trayectos = Trayecto.objects.all()
        trayectos_serializer = TrayectoListSerializer(trayectos, many=True)
        return Response(trayectos_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        trayecto_serializer = TrayectoSerializer(data=request.data)
        if trayecto_serializer.is_valid():
            trayecto_serializer.save()
            return Response({'message': 'Trayecto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(trayecto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def trayecto_detail_api_view(request, id=None):
    # queryset
    trayecto = Trayecto.objects.filter(id=id).first()

    # validation
    if trayecto:

        # retrieve
        if request.method == 'GET':
            trayecto_serializer = TrayectoListSerializer(trayecto)
            return Response(trayecto_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            trayecto_serializer = TrayectoSerializer(
                trayecto, data=request.data)
            if trayecto_serializer.is_valid():
                trayecto_serializer.save()
                return Response(trayecto_serializer.data, status=status.HTTP_200_OK)
            return Response(trayecto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            trayecto.delete()
            return Response({'message': 'Trayecto Eliminado correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
