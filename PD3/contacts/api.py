from rest_framework.decorators import action
from rest_framework.response import Response

from contacts.models import Person, Address, Email, Phone
from contacts.serializers import PersonSerializer, AddressSerializer, EmailSerializer, PhoneSerializer
from rest_framework import generics, viewsets, renderers


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=False, renderer_classes=[renderers.JSONRenderer])
    def pesel(self, request, *args, **kwargs):
        obj = {1, 2, 3, 4, 5}
        return Response(obj)

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class EmailList(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class EmailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class PhoneList(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer