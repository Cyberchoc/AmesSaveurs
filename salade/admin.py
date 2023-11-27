from django.contrib import admin
from .models import Salade

class SaladeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom']

# Register your models here.

admin.site.register(Salade, SaladeAdmin)