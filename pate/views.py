from django.shortcuts import render, get_object_or_404
from .models import Pate
import pandas as pd

# Create your views here.

def index(request):
    pates = Pate.objects.all().order_by('nom')

    pate_data = {
        'nom': [pate.nom for pate in pates],
        'prix': [pate.prix for pate in pates],
        'ingredients': [pate.ingredients for pate in pates],
        'vegetarienne': [pate.vegetarienne for pate in pates],
        'stock': [pate.stock for pate in pates],
        'image': [pate.thumbnail for pate in pates],
    }
    df_pate  = pd.DataFrame(pate_data)

    nombre_total_pates = len(df_pate)
    prix_moyen_pates = round(df_pate['prix'].mean(), 2) 

    filtre_vegetarienne_pates = (df_pate['vegetarienne'] == True)
    nombre_vegetarienne_pates = df_pate.loc[filtre_vegetarienne_pates, 'nom'].count()


    return render(request, 'pate/index.html', {'pates' : pates,
                                               'nombre_total_pates' : nombre_total_pates,
                                               'prix_moyen_pates' : prix_moyen_pates,
                                               'nombre_vegetarienne_pates' : nombre_vegetarienne_pates})


def pate_detail(request, pate_id):
    pate = get_object_or_404(Pate, pk=pate_id)
    return render(request, 'pate/pate_detail.html', {'pate': pate})