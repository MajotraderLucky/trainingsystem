from django.db import models
from django.contrib.auth.models import User
from .models import Product

class Product(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()

class ProductAccess(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)