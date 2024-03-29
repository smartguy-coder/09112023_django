# Generated by Django 5.0.2 on 2024-02-15 17:31

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('1.00'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=160, unique=True),
        ),
    ]
