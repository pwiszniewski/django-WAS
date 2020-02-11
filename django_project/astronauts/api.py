from rest_framework.decorators import action
from rest_framework.response import Response

from astronauts.models import Astronaut
from astronauts.serializers import AstronautSerializer
from rest_framework import generics, viewsets, renderers


class AstronautList(generics.ListCreateAPIView):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer


class AstronautDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer


class AstronautViewSet(viewsets.ModelViewSet):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer

    @action(detail=False, renderer_classes=[renderers.JSONRenderer])
    def pesel(self, request, *args, **kwargs):
        obj = {1, 2, 3, 4, 5}
        return Response(obj)