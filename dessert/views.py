from django.shortcuts import render, get_object_or_404
from .models import Dessert

# Create your views here.

def index(request):
    desserts = Dessert.objects.all().order_by('nom')
    return render(request, 'dessert/index.html', {'desserts' : desserts})


def dessert_detail(request, dessert_id):
    dessert = get_object_or_404(Dessert, pk=dessert_id)
    return render(request, 'dessert/dessert_detail.html', {'dessert': dessert})