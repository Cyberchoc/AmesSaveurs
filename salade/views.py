from django.shortcuts import render, get_object_or_404
from .models import Salade
import pandas as pd

# Create your views here.

def index(request):
    salades = Salade.objects.all().order_by('nom')

    salade_data = {
        'nom': [salade.nom for salade in salades],
        'prix': [salade.prix for salade in salades],
        'ingredients': [salade.ingredients for salade in salades],
        'vegetarienne': [salade.vegetarienne for salade in salades],
        'stock': [salade.stock for salade in salades],
        'image': [salade.thumbnail for salade in salades],
    }
    df_salade  = pd.DataFrame(salade_data)

    nombre_total_salades = len(df_salade)
    prix_moyen_salades = round(df_salade['prix'].mean())
    
    filtre_vegetarienne_salades = (df_salade['vegetarienne'] == True)
    nombre_vegetarienne_salades = df_salade.loc[filtre_vegetarienne_salades, 'nom'].count()   

    return render(request, 'salade/index.html', {'salades' : salades,
                                               'nombre_total_salades' : nombre_total_salades,
                                               'prix_moyen_salades' : prix_moyen_salades,
                                               'nombre_vegetarienne_salades' : nombre_vegetarienne_salades})

def salade_detail(request, salade_id):
    salade = get_object_or_404(Salade, pk=salade_id)
    return render(request, 'salade/salade_detail.html', {'salade': salade})