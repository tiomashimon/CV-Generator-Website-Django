from django.db import models


class Profiel(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


