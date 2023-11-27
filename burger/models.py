from django.db import models

# Create your models here.

class Burger(models.Model):
    nom = models.CharField(max_length=128)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="burger/static/burger/images", blank=True, null=True)
    
    def __str__(self):
        return self.nom