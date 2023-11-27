from django.db import models

# Create your models here.

class Salade(models.Model):
    nom = models.CharField(max_length=128)
    #slug = models.SlugField(max_length=128)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="salade/static/salade/images", blank=True, null=True)
    
    def __str__(self):
        return self.nom