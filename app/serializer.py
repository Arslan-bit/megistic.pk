from rest_framework import serializers
from .models import Delivery,Product,Status,Payments
import random
from .models import  Delivery
from django.db import models

from rest_framework.fields import CurrentUserDefault





class DeliverySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Delivery
        fields = '__all__'
        fields = ['user','product','description','image','quantity']

    def create(self, validated_data):
        delivery = Delivery.objects.create(
            user=validated_data['user'],
            product=validated_data['product'],
            description=validated_data['description'],
            image=validated_data['image'],
            quantity=validated_data['quantity'],
            Delivery_id=random.randint(100000, 999999),
            )
        
        delivery.save()

        return delivery
        



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(
            product_name=validated_data['product_name'],
            description=validated_data['description'],
            image=validated_data['image'],
            price=validated_data['price'],
            stock=validated_data['stock'],
            )
        
        product.save()

        return product
    

class StatusSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Status
        fields = '__all__'

    def create(self, validated_data):
        status = Status.objects.create(
            deliver_user=validated_data['deliver_user'],
            Status=validated_data['Status']
            )
        
        status.save()

        return status
        





class PaymentsSerializer(serializers.ModelSerializer):
    # deliver_user = serializers.PrimaryKeyRelatedField(queryset=Delivery.objects.filter(user = CurrentUserDefault()))
   
    class Meta:
        model = Payments
        fields = '__all__'

    def create(self, validated_data):
        payments = Payments.objects.create(
            price=validated_data['price'],
            image=validated_data['image'],
            delivery=validated_data['delivery'],
            record_file=validated_data['record_file'],
            User=CurrentUserDefault()
            
            )
        
        payments.save()
        return payments



        
        



