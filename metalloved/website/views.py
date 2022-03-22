from django.shortcuts import render
from .models import Card


def home_page(request):
    cards = Card.objects.all()
    prices = Card.objects.values('price')
    for price in prices:
        print(price)
    #     if isinstance(price, dict):
    #         new_card_price = f"{price} + '₽' "
    #         print(new_card_price)

    return render(request, 'website/index.html', {'cards': cards})
