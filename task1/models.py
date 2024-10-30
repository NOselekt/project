from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=37)
    balance = models.DecimalField(decimal_places=3, max_digits=9)
    age = models.PositiveIntegerField()

class Game(models.Model):
    title = models.CharField(max_length=127)
    cost = models.DecimalField(decimal_places=3, max_digits=9)
    size = models.DecimalField(decimal_places=3, max_digits=9)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="games")

# Buyer.objects.create(name="Gabe", balance=999999, age=61)
# Buyer.objects.create(name="Vitaliy", balance=10000, age=44)
# Buyer.objects.create(name="Misha", balance=10000, age=17)
# Game.objects.create(title="Cyberpunk 2077", cost=60, size=100, description="New bug has been fixed!", age_limited=False)
# vitalya=Buyer.objects.get(id=2)
# gaben=Buyer.objects.get(id=1)
# misha=Buyer.objects.get(id=3)
# Game.objects.get(id=1).buyer.set((gaben, vitalya))
# Game.objects.create(title="Nier: Automata", cost=30, size=40, description="New android has been killed!", age_limited=True)
# Game.objects.create(title="Super Mario", cost=70, size=30, description="New mushroom has been eaten!", age_limited=False)
# Game.objects.get(id=2).buyer.set((vitalya,))
# Game.objects.get(id=3).buyer.set((gaben, vitalya, misha))