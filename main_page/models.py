from django.db import models

# Create your models here.


class Curiosity(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField(name="text", default="")


