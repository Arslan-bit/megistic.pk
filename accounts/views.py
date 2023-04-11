
from .serializer import (
    RegistrationSerializer
)
from rest_framework.viewsets import (
    generics
)
from rest_framework import permissions


# create Register Form
class RegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer


