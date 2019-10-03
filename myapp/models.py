from __future__ import unicode_literals
from django.db import models
from django.db.models.constraints import UniqueConstraint


from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=50)


class Reserve(models.Model):
    name=models.CharField(max_length=100)
    dt=models.DateField(auto_now_add=False)
    tt=models.CharField(max_length=30)
    tableno=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()

    class Meta:
        db_table="reserve"
        unique_together =['tableno','tt','dt']
