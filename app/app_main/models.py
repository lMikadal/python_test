from django.db import models

# Create your models here.

class Good(models.Model):
    title = models.CharField(max_length=100)
    stock = models.IntegerField()
