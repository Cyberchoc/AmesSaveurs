from django.db import models

# Create your models here.

class Pizza(models.Model):
    nom = models.CharField(max_length=128)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    #prix_senior = models.FloatField(default=0)
    #prix_mega = models.FloatField(default=0)
    pizza_base_tomate = models.BooleanField(default=False)
    pizza_base_creme = models.BooleanField(default=False)
    vegetarienne = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="pizza/static/pizza/images", blank=True, null=True)
    
    def __str__(self):
        return self.nom