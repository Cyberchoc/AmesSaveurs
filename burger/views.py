from django.shortcuts import render, get_object_or_404
from .models import Burger
import pandas as pd

# Create your views here.

def index(request):
    burgers = Burger.objects.all().order_by('prix')
    
    burger_data  = {
        'nom': [burger.nom for burger in burgers],
        'prix': [burger.prix for burger in burgers],
        'ingredients': [burger.ingredients for burger in burgers],
        'vegetarienne': [burger.vegetarienne for burger in burgers],
        'stock': [burger.stock for burger in burgers],
        'image': [burger.thumbnail for burger in burgers],
    }
    df_burger  = pd.DataFrame(burger_data)

    nombre_total_burger = len(df_burger)
    prix_moyen_burger = round(df_burger['prix'].mean(), 2)

    filtre_vegetarienne_burgers = (df_burger['vegetarienne'] == True)
    nombre_vegetarienne_burgers = df_burger.loc[filtre_vegetarienne_burgers, 'nom'].count()
    
    return render(request, 'burger/index.html', {'burgers' : burgers,
                                               'nombre_total_burger' : nombre_total_burger,
                                               'prix_moyen_burger' : prix_moyen_burger,
                                               'nombre_vegetarienne_burgers' : nombre_vegetarienne_burgers})


def pate_detail(request, burger_id):
    burger = get_object_or_404(Burger, pk=burger_id)
    return render(request, 'burger/burger_detail.html', {'burger': burger})