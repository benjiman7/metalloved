# Generated by Django 4.0.2 on 2022-03-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, default='default.svg', upload_to='website/static/images/media'),
        ),
    ]