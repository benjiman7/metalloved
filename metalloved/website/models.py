from django.db import models


# TODO: change charfield to textfield for description
# TODO: smth with price

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # photo = models.ImageField(upload_to='static/images/photos/')
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    pass
