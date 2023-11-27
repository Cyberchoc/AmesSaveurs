from django.shortcuts import render, get_object_or_404
from .models import Burger

# Create your views here.

def index(request):
    burgers = Burger.objects.all().order_by('prix')
    return render(request, 'burger/index.html', {'burgers' : burgers})


def pate_detail(request, burger_id):
    burger = get_object_or_404(Burger, pk=burger_id)
    return render(request, 'burger/burger_detail.html', {'burger': burger})