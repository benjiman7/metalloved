from django.shortcuts import render
from .models import Card


def home_page(request):
    cards = Card.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        message = request.POST['message']
        return render(request, 'website/index.html', {'cards': cards})

    else:
        pass

    return render(request, 'website/index.html', {'cards': cards})
