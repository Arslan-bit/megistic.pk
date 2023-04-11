
from .serializer import (
    DeliverySerializer,PaymentsSerializer
)
from rest_framework.viewsets import (
    generics
)
from rest_framework import permissions
from .models import Payments,Delivery
from django.http import HttpResponse

# create Register Form
# user site
class DeliveryView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DeliverySerializer
    



# user site
class PaymentsView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentsSerializer
    # queryset = Delivery.objects.all()

    def get_queryset(self):
        data = Delivery.objects.filter(user=self.request.user)
        return data
    
    def get_context_data(self, **kwargs):
        return Delivery.objects.filter(user=self.request.user)
    

def index(request):
    
    return HttpResponse('First Project API Congratulations!')


