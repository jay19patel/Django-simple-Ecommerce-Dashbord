from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Products(models.Model):
    CATEGORY = (
        ('Indore','Indore'),
        ('Out Door','Out Door'),

    )
    name=models.CharField(max_length=100)
    price = models.FloatField(null=True)
    category =models.CharField(max_length=100,choices=CATEGORY)
    description =models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tag= models.ManyToManyField(Tag)
      
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Panding','Panding'),
        ('Out of Delivery','Out of Delivery'),
        ('Delivered','Delivered'),

    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=100,null=True ,choices=STATUS)
    def __str__(self):
        return self.status