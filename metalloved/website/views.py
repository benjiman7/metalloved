from django.shortcuts import render
from .models import Card


def home_page(request):
    cards = Card.objects.all()
    # print(cards)
    # prices = Card.objects.values('price')
    # print(prices)
    # clear_prices = {}
    # for price in prices:
    #     clear_prices['new_price'] = price['price']
    #     # clear_prices.append(clear_prices)
    
    # print(clear_prices)
    
    return render(request, 'website/index.html', {'cards': cards})
