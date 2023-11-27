from django.shortcuts import render, get_object_or_404
from .models import Salade

# Create your views here.

def index(request):
    salades = Salade.objects.all().order_by('nom')
    return render(request, 'salade/index.html', {'salades' : salades})

def salade_detail(request, salade_id):
    salade = get_object_or_404(Salade, pk=salade_id)
    return render(request, 'salade/salade_detail.html', {'salade': salade})