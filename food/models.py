from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/products/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(unique=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    payment_type = models.IntegerField(null=False, blank=False, default=1)
    status = models.IntegerField(null=False, blank=True, default=0)
    address = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class OrderProduct(models.Model):
    count = models.IntegerField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)