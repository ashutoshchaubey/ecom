from __future__ import unicode_literals
from django.db import models
from .forms import ContactForm, SignUpForm
from django.conf import settings
from django.views import generic
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

User = settings.AUTH_USER_MODEL

# Create your models here.

class Products(models.Model):
    TYPE_CHOICES = (
        ('Blouse', 'Blouse'),
        ('Shirts', 'Shirt'),
        ('Skirts', 'Skirt'),
        ('Gown', 'Gown'),
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 10, default=19.99)
    items_type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Skirts')
    image = models.ImageField(default = 'cover.jpg')
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Profile(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    products = models.ManyToManyField(Products, blank=True)

    def __unicode__(self):
        return self.name

class Blouse(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    half_length = models.DecimalField(max_digits=10, decimal_places=2)
    ub_length = models.DecimalField(max_digits=10, decimal_places=2)
    ub_width = models.DecimalField(max_digits=10, decimal_places=2)
    sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    round_sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    tf_sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    long_sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    shoulder = models.DecimalField(max_digits=10, decimal_places=2)

class Shirts(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    half_length = models.DecimalField(max_digits=10, decimal_places=2)
    ub_length = models.DecimalField(max_digits=10, decimal_places=2)
    ub_width = models.DecimalField(max_digits=10, decimal_places=2)
    sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    round_sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    tf_sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    long_sleeve = models.DecimalField(max_digits=10, decimal_places=2)
    shoulder = models.DecimalField(max_digits=10, decimal_places=2)

class Skirts(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    knee_length = models.DecimalField(max_digits=10, decimal_places=2)

class Gowns(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    long_length = models.DecimalField(max_digits=10, decimal_places=2)
    short_length = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=1)

class Specifications(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, blank=True)
    blouse = models.ForeignKey(Blouse, null = True, blank=True, on_delete=models.CASCADE)
    shirts = models.ForeignKey(Shirts, null = True, blank=True, on_delete=models.CASCADE)
    skirts = models.ForeignKey(Skirts, null = True, blank=True, on_delete=models.CASCADE)
    gowns = models.ForeignKey(Gowns, null = True, blank=True, on_delete=models.CASCADE)

class Content(models.Model):
    image = models.ImageField(upload_to = 'content/')
    name_of_item = models.CharField(max_length=300)
    specifications = models.ForeignKey(Specifications, null = True, blank=True, on_delete=models.CASCADE)

class OrderItem(models.Model):
    products = models.OneToOneField(Products, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.products.title

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(null=True)

    def get_cart_items(self):
        return self.items.all