from django.db import models

class Animal(models.Model):
    latinName = models.CharField(max_length=120)
