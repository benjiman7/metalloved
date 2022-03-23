from django.shortcuts import render
from .models import Card


def home_page(request):
    cards = Card.objects.all()
    prices = Card.objects.values('price')
    new_price = {
        'new_price': ['5000', '', '7000']
    }
    x = new_price['new_price']
    print(x)
    for y in x:
        print(y)
    # for price in new_price:
    #     for price1 in price:
    #         print(price1)
    #     new_price.update({'new_price': price})
    #     if len(price.get('price')) < 1:
    #         print(True)
    #     else:
    #         print(False)

    return render(request, 'website/index.html', {'cards': cards, 'new_price': new_price})
