from django.shortcuts import render, get_object_or_404
from .models import Pizza

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all().order_by('nom')
    return render(request, 'pizza/index.html', {'pizzas' : pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    return render(request, 'pizza/pizza_detail.html', {'pizza': pizza})