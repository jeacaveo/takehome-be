from rest_framework import viewsets

from api.models import House
from api.serializers import HouseSerializer


class HouseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = House.objects.all()
    serializer_class = HouseSerializer
