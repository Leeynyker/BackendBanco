from rest_framework import viewsets

from .models import product
from .serializers import productSerializer
# Create your views here.


class productViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = productSerializer
    queryset = product.objects.all()