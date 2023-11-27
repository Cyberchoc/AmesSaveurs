from django.shortcuts import render, get_object_or_404
from .models import Pate

# Create your views here.

def index(request):
    pates = Pate.objects.all().order_by('nom')
    return render(request, 'pate/index.html', {'pates' : pates})


def pate_detail(request, pate_id):
    pate = get_object_or_404(Pate, pk=pate_id)
    return render(request, 'pate/pate_detail.html', {'pate': pate})