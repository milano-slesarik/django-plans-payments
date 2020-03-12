# Generated by Django 3.2.15 on 2022-12-08 10:07

from decimal import Decimal
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('plans_payments', '0002_payment_transaction_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='billing_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_fee',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=9),
        ),
    ]