from django.shortcuts import render
from django.http import HttpResponse
from affiche_menu.models import AfficheMenu
from pizza.models import Pizza
from burger.models import Burger
from salade.models import Salade
from dessert.models import Dessert
from pate.models import Pate
import pandas as pd


# Create your views here.

def index(request):
    affiches_menus = AfficheMenu.objects.all()
    pizzas = Pizza.objects.all()
    burgers = Burger.objects.all()
    salades = Salade.objects.all()
    desserts = Dessert.objects.all()
    pates = Pate.objects.all()

    # Créer un dictionnaire avec les données
    pizza_data  = {
        'nom': [pizza.nom for pizza in pizzas],
        'prix': [pizza.prix for pizza in pizzas],
        'ingredients': [pizza.ingredients for pizza in pizzas],
        'pizza_base_tomate': [pizza.pizza_base_tomate for pizza in pizzas],
        'pizza_base_creme': [pizza.pizza_base_creme for pizza in pizzas],
        'vegetarienne': [pizza.vegetarienne for pizza in pizzas],
        'stock': [pizza.stock for pizza in pizzas],
        'image': [pizza.thumbnail for pizza in pizzas],
    }
    
    
    burger_data  = {
        'nom': [burger.nom for burger in burgers],
        'prix': [burger.prix for burger in burgers],
        'ingredients': [burger.ingredients for burger in burgers],
        'vegetarienne': [burger.vegetarienne for burger in burgers],
        'stock': [burger.stock for burger in burgers],
        'image': [burger.thumbnail for burger in burgers],
    }
    
    
    salade_data = {
        'nom': [salade.nom for salade in salades],
        'prix': [salade.prix for salade in salades],
        'ingredients': [salade.ingredients for salade in salades],
        'vegetarienne': [salade.vegetarienne for salade in salades],
        'stock': [salade.stock for salade in salades],
        'image': [salade.thumbnail for salade in salades],
    }
    
    
    dessert_data = {
        'nom': [dessert.nom for dessert in desserts],
        'prix': [dessert.prix for dessert in desserts],
        'ingredients': [dessert.ingredients for dessert in desserts],
        'vegetarienne': [dessert.vegetarienne for dessert in desserts],
        'stock': [dessert.stock for dessert in desserts],
        'image': [dessert.thumbnail for dessert in desserts],
    }
    
    
    pate_data = {
        'nom': [pate.nom for pate in pates],
        'prix': [pate.prix for pate in pates],
        'ingredients': [pate.ingredients for pate in pates],
        'vegetarienne': [pate.vegetarienne for pate in pates],
        'stock': [pate.stock for pate in pates],
        'image': [pate.thumbnail for pate in pates],
    }
    
    # Créer le DataFrame
    df_pizza  = pd.DataFrame(pizza_data)
    df_burger  = pd.DataFrame(burger_data)
    df_salade  = pd.DataFrame(salade_data)
    df_dessert  = pd.DataFrame(dessert_data)
    df_pate  = pd.DataFrame(pate_data)

    # Calcules
    nombre_total_pizzas = len(df_pizza)
    prix_moyen_pizzas = df_pizza['prix'].mean()

    nombre_total_burger = len(df_burger)
    prix_moyen_burger = df_burger['prix'].mean()

    nombre_total_salades = len(df_salade)
    prix_moyen_salades = df_salade['prix'].mean()

    nombre_total_desserts = len(df_dessert)
    prix_moyen_desserts = df_dessert['prix'].mean()

    nombre_total_pates = len(df_pate)
    prix_moyen_pates = df_pate['prix'].mean()

    filtre_vegetarienne_pizzas = (df_pizza['vegetarienne'] == True)
    nombre_vegetarienne_pizzas = df_pizza.loc[filtre_vegetarienne_pizzas, 'nom'].count()

    filtre_vegetarienne_burgers = (df_burger['vegetarienne'] == True)
    nombre_vegetarienne_burgers = df_burger.loc[filtre_vegetarienne_burgers, 'nom'].count()
    
    filtre_vegetarienne_salades = (df_salade['vegetarienne'] == True)
    nombre_vegetarienne_salades = df_salade.loc[filtre_vegetarienne_salades, 'nom'].count()    

    filtre_vegetarienne_desserts = (df_dessert['vegetarienne'] == True)
    nombre_vegetarienne_desserts = df_dessert.loc[filtre_vegetarienne_desserts, 'nom'].count()    

    filtre_vegetarienne_pates = (df_pate['vegetarienne'] == True)
    nombre_vegetarienne_pates = df_pate.loc[filtre_vegetarienne_pates, 'nom'].count()

    

    return render(request, 'main/index.html', {'prix_moyen_pizzas' : prix_moyen_pizzas,
                                               'nombre_total_pizzas' : nombre_total_pizzas,
                                               'affiches_menus' : affiches_menus,
                                                 'pizzas' : pizzas,
                                                   'burgers' : burgers,
                                                     'salades' : salades,
                                                       'desserts' : desserts,
                                                         'pates' : pates,
                                               'nombre_total_burger' : nombre_total_burger,
                                               'prix_moyen_burger' : prix_moyen_burger,
                                               'nombre_total_salades' : nombre_total_salades,
                                               'prix_moyen_salades' : prix_moyen_salades,
                                               'nombre_total_desserts' : nombre_total_desserts,
                                               'prix_moyen_desserts' : prix_moyen_desserts,
                                               'nombre_total_pates' : nombre_total_pates,
                                               'prix_moyen_pates' : prix_moyen_pates,
                                               'nombre_vegetarienne_pizzas' : nombre_vegetarienne_pizzas,
                                               'nombre_vegetarienne_burgers' : nombre_vegetarienne_burgers,
                                               'nombre_vegetarienne_salades' : nombre_vegetarienne_salades,
                                               'nombre_vegetarienne_desserts' : nombre_vegetarienne_desserts,
                                               'nombre_vegetarienne_pates' : nombre_vegetarienne_pates})

