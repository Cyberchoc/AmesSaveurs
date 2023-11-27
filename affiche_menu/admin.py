from django.contrib import admin

from .models import AfficheMenu

class AfficheMenuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'thumbnail')
    search_fields = ['nom']

# Register your models here.

admin.site.register(AfficheMenu, AfficheMenuAdmin)