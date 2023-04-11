from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager



class User(AbstractUser):

    
    phone_number=models.CharField(max_length=11,unique=True)
    
    USERNAME_FIELD = 'phone_number'
    image=models.ImageField(upload_to='profiles/',blank=True)
    REQUIRED_FIELDS=[]
    object = UserManager()


    # is_phone_number = models.BooleanField(default=False)
    # otp=models.CharField(max_length=6)
    # image=models.ImageField(upload_to='media/qrcode',blank=True)
    
