
from .serializer import (
    ProductSerializer,StatusSerializer
)
from rest_framework.viewsets import (
    generics
)
from rest_framework import permissions


# admin site
class ProductView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    

# Admin site
class StatusView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StatusSerializer


