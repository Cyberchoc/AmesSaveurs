from django.shortcuts import render, get_object_or_404
from .models import Pizza
import pandas as pd

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all().order_by('nom')
    
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
    df_pizza  = pd.DataFrame(pizza_data)

    nombre_total_pizzas = len(df_pizza)
    prix_moyen_pizzas = round(df_pizza['prix'].mean(), 2)

    filtre_vegetarienne_pizzas = (df_pizza['vegetarienne'] == True)
    nombre_vegetarienne_pizzas = df_pizza.loc[filtre_vegetarienne_pizzas, 'nom'].count()

    return render(request, 'pizza/index.html', {'pizzas' : pizzas,
                                                'prix_moyen_pizzas' : prix_moyen_pizzas,
                                               'nombre_total_pizzas' : nombre_total_pizzas,
                                               'nombre_vegetarienne_pizzas' : nombre_vegetarienne_pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    return render(request, 'pizza/pizza_detail.html', {'pizza': pizza})