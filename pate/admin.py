from django.contrib import admin
from .models import Pate

class PateAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom']

# Register your models here.

admin.site.register(Pate, PateAdmin)