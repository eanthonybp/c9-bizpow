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
    

