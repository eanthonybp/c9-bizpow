from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Survey(models.Model):
    biggest_problem = models.CharField(max_length=255)
    email_contact = models.EmailField(max_length=75)
    def __str__(self):
        return self.email_contact + " : " + self.biggest_problem
    

