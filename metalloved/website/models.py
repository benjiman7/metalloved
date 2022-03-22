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
        return f"{self.title}"


class ContactForm(models.Model):
    pass
