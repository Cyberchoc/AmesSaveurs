from django.shortcuts import render
from django.http import HttpResponse
from affiche_menu.models import AfficheMenu
from pizza.models import Pizza
from burger.models import Burger
from salade.models import Salade
from dessert.models import Dessert
from pate.models import Pate

# Create your views here.

def index(request):
    affiches_menus = AfficheMenu.objects.all()
    pizzas = Pizza.objects.all()
    burgers = Burger.objects.all()
    salades = Salade.objects.all()
    desserts = Dessert.objects.all()
    pates = Pate.objects.all()

    all_noms = []
    for i in pizzas:
        image = i.nom
        all_noms.append(image)
        
    for i in burgers:
        image = i.nom
        all_noms.append(image)

    for i in desserts:
        image = i.nom
        all_noms.append(image)
        
    for i in salades:
        image = i.nom
        all_noms.append(image)
        
    for i in pates:
        image = i.nom
        all_noms.append(image)

    return render(request, 'main/index.html', {'affiches_menus' : affiches_menus, 'pizzas' : pizzas, 'images' : all_noms, 'burgers' : burgers, 'salades' : salades, 'desserts' : desserts, 'pates' : pates})

