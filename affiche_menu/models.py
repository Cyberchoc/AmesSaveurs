from django.db import models

# Create your models here.

class AfficheMenu(models.Model):
    nom = models.CharField(max_length=128)
    thumbnail = models.ImageField(upload_to="affiche_menu/static/affiche_menu/images", blank=True, null=True)
    
    def __str__(self):
        return self.nom