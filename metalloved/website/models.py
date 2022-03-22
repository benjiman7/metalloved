from locale import currency
from django.db import models


# TODO: add description in admin panel for price and currency

class Card(models.Model):
    RUB = '₽'
    NONE = 'Договорная'
    CURRENCY_CHOICES = [(RUB, '₽'), (NONE, 'Договорная')]
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, default='default.svg')
    price = models.CharField(max_length=255, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, default=RUB, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class ContactForm(models.Model):
    pass
