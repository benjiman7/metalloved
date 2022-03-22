# Generated by Django 4.0.2 on 2022-03-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_card_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='currency',
            field=models.CharField(choices=[('₽', '₽'), ('-', '-')], default='₽', max_length=10),
        ),
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
