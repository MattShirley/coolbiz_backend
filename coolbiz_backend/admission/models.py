from django.db import models

class Admission(models.Model):
    #'username', 'first_name', 'last_name',)
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)