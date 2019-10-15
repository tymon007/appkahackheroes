from django.db import models

# Create your models here.


class Ciekawostki(models.Model):
    liczbaporzadkowa = models.CharField(max_length=200)
    ciekawostka = models.TextField(name="ciekawostka")


