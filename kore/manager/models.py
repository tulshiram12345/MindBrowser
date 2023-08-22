from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Manager(models.Model):
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    dob = models.DateField()
    company = models.CharField(max_length=300)

    def __str__(self):
        return self.firstname+" "+self.lastname


class Employee(models.Model):
    empid = models.CharField(max_length=10, unique=True)
    mobile = models.CharField(max_length=10)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    company = models.CharField(max_length=300)

    def __str__(self):
        return self.firstname+" "+self.lastname
