from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
