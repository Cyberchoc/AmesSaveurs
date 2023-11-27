
from django.shortcuts import render
from .models import AfficheMenu

# Create your views here.

def index(request):
    affiches_menus = AfficheMenu.objects.all().order_by('nom')
    return render(request, 'affiche_menu/index.html', {'affiches_menus' : affiches_menus})
