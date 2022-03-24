from django.shortcuts import render
from .models import Card


def home_page(request):
    cards = Card.objects.all()
    
    return render(request, 'website/index.html', {'cards': cards})
