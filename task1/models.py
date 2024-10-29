from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=37)
    balance = models.DecimalField(decimal_places=6, max_digits=6)
    age = models.PositiveIntegerField()

class Game(models.Model):
    title = models.CharField(max_length=127)
    cost = models.DecimalField(decimal_places=6, max_digits=6)
    size = models.DecimalField(decimal_places=3, max_digits=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="games")
