from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'pizza_base_creme', 'pizza_base_tomate', 'prix')
    search_fields = ['nom']

# Register your models here.

admin.site.register(Pizza, PizzaAdmin)