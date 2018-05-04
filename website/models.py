from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class Survey(models.Model):
    biggest_problem = models.CharField(max_length=255)
    email_contact = models.EmailField(max_length=75)
    submitted = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.email_contact + " : " + self.biggest_problem
    
class UserProfile(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    emailAddress = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    created = models.DateTimeField(default=datetime.now)
    account = models.ForeignKey('Account')
    
class Account(models.Model):
    accountName = models.CharField(max_length=50)
    industry = models.ForeignKey('Industry')
    
class Industry(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)
    
    
