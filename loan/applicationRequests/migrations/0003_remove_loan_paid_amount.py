# Generated by Django 4.2 on 2023-04-18 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("applicationRequests", "0002_loan_paid_amount"),
    ]

    operations = [
        migrations.RemoveField(model_name="loan", name="paid_amount",),
    ]
