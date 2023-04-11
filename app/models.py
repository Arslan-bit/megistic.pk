from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User
from django.core.validators import FileExtensionValidator


class Product(models.Model):
    product_name = models.CharField(null=True, blank=True, max_length=30)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='stock/')
    price = models.IntegerField()
    stock = models.IntegerField()

    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-create']

    def __str__(self):
        return str([self.product_name, self.price, self.stock])


class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField()
    Delivery_id = models.IntegerField(blank=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-create']

    def __str__(self):
        return str([self.product, self.quantity, self.user, self.create])


class Status(models.Model):
    PRODUCT = (
        ('pending', 'pending'),
        ('slected', 'slected'),
        ('deliver', 'deliver'),
        ('return', 'return'),
    )
    deliver_user = models.ForeignKey(to=Delivery, on_delete=models.CASCADE)
    Status = models.CharField(max_length=10, choices=PRODUCT, default='P')
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-create']

    def __str__(self):
        return str([self.deliver_user, self.Status, self.create])


class Payments(models.Model):

    price = models.IntegerField()
    delivery = models.OneToOneField(Delivery, on_delete = models.CASCADE)
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')
    record_file = models.FileField(upload_to='deliver_records/' ,validators=[FileExtensionValidator(allowed_extensions=(['XLSX']))])
                             
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-create']

    def __str__(self):
        return str([self.delivery])

