# Generated by Django 4.0.2 on 2022-03-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_card_image_alter_card_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, default='default.svg', upload_to='media'),
        ),
    ]