from django.db import models
from django.conf import settings
from ecom.models import Products, Cart


User = settings.AUTH_USER_MODEL

# Create your models here.
class Billings(models.Model):
	full_name = models.CharField(max_length = 100)
	email = models.EmailField(max_length=254)
	billing_addr = models.CharField(max_length=500)
	shipping_addr = models.CharField(max_length=500)
	pincode = models.IntegerField()
	phone_number = models.IntegerField()


class Content(models.Model):
    image = models.ImageField(upload_to = 'content/')
    name_of_item = models.CharField(max_length=300)

