from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, min_length=8, write_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ["first_name", 'last_name','username', 'phone_number', 'password','image']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

