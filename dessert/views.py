from django.shortcuts import render, get_object_or_404
from .models import Dessert
import pandas as pd

# Create your views here.

def index(request):
    desserts = Dessert.objects.all().order_by('nom')
    
    dessert_data = {
        'nom': [dessert.nom for dessert in desserts],
        'prix': [dessert.prix for dessert in desserts],
        'ingredients': [dessert.ingredients for dessert in desserts],
        'vegetarienne': [dessert.vegetarienne for dessert in desserts],
        'stock': [dessert.stock for dessert in desserts],
        'image': [dessert.thumbnail for dessert in desserts],
    }
    df_dessert  = pd.DataFrame(dessert_data)

    nombre_total_desserts = len(df_dessert)
    prix_moyen_desserts = round(df_dessert['prix'].mean(), 2)

    filtre_vegetarienne_desserts = (df_dessert['vegetarienne'] == True)
    nombre_vegetarienne_desserts = df_dessert.loc[filtre_vegetarienne_desserts, 'nom'].count()   
    
    return render(request, 'dessert/index.html', {'desserts' : desserts,
                                               'nombre_total_desserts' : nombre_total_desserts,
                                               'prix_moyen_desserts' : prix_moyen_desserts,
                                               'nombre_vegetarienne_desserts' : nombre_vegetarienne_desserts})


def dessert_detail(request, dessert_id):
    dessert = get_object_or_404(Dessert, pk=dessert_id)
    return render(request, 'dessert/dessert_detail.html', {'dessert': dessert})