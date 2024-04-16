# models.py
from django.db import models

class CropParameters(models.Model):
    N = models.FloatField()
    P = models.FloatField()
    K = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    crop_type=models.CharField(max_length=100,blank=True)
class CropParametersCollect(models.Model):
    N = models.FloatField()
    P = models.FloatField()
    K = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    crop_type=models.CharField(max_length=100,blank=True)