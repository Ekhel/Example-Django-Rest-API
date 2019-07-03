from django.db import models

class Nelayan(models.Model):
    nama = models.CharField(max_length=50)
    umur = models.CharField(max_length=50)
    distrik = models.CharField(max_length=50)
    kampung = models.CharField(max_length=50)
