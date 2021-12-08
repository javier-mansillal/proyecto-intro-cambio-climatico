from django.db import models

# Create your models here.

class Co2(models.Model):
    año = models.IntegerField()
    actividad = models.CharField(max_length=30)
    cantidad = models.FloatField()