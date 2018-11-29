from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15)
    Remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    material_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    Remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.material_name


class Account(models.Model):
    customer_name = models.ForeignKey(Customers)
    date = models.DateField(blank=True, null=True)
    material_name = models.ForeignKey(Material)
    quantity = models.IntegerField()
    Remark = models.CharField(max_length=200, blank=True)

    @property
    def total(self):
        return self.material_name.price * self.quantity

    def __str__(self):
        return self.customer_name.name
