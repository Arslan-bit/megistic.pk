
from django.urls import path

from .views import DeliveryView,PaymentsView
from .views_admin import ProductView,StatusView
    

urlpatterns = [
    
    path('api/delivery/', DeliveryView.as_view(), name='delivery'),
    path('api/product/', ProductView.as_view(), name='product'),
    path('api/payment/', PaymentsView.as_view(), name='payment'),
    path('api/status/', StatusView.as_view(), name='status')
    
]