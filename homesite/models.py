from django.db import models


class Fabric(models.Model):
    fabric_name = models.CharField(max_length=100)
    quantity = models.FloatField()

    def __str__(self):
        return self.fabric_name


class Cutting(models.Model):
    fabric_name = models.CharField(max_length=100)
    cutting_type = models.CharField(max_length=200)
    weight = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.cutting_type


class StockEntry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=100)
    fabric_name = models.CharField(max_length=100)
    cutting_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.entry_id


class Worker(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()
    balance = models.FloatField()
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.payment_id


class Variance(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    variance = models.FloatField()
    fabric_name = models.CharField(max_length=100)

    def __str__(self):
        return self.date


class Sewing(models.Model):
    fabric_name = models.CharField(max_length=100)
    cutting_type = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.cutting_type


class Packing(models.Model):
    fabric_name = models.CharField(max_length=100)
    cutting_type = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.cutting_type


class Invoice(models.Model):
    entry_id = models.AutoField(primary_key=True)
    invoice_no = models.CharField(max_length=10)
    fabric_name = models.CharField(max_length=100)
    cutting_type = models.CharField(max_length=200)
    quantity = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.entry_id
