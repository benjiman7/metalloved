from atexit import register
from turtle import title
from django.db import models


# TODO: change charfield to textfield for description
# TODO: smth with price

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, default='default.svg')
    price = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_price (request):
        cards = request
        card_price = cards.price

        if isinstance(card_price, str):
            return f"{card_price} + '₽' "
        else:
            return f"{card_price}"

class ContactForm(models.Model):
    pass
