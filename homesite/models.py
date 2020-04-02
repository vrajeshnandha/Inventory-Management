from django.db import models


# Create your models here.

class Fabric(models.Model):
    fabric_name = models.CharField(max_length=100)
    quantity = models.FloatField()

    def __str__(self):
        return self.fabric_name


class Cutting(models.Model):
    fabric_name = models.CharField(max_length=100)
    cutting_type = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.cutting_type
