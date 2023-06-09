# Generated by Django 4.2 on 2023-04-19 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applicationRequests", "0004_loan_date_loan_payment_per_month"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="installment_date",
            field=models.DateField(default=datetime.date(2022, 4, 20)),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateField(default=datetime.date(2022, 4, 20)),
        ),
    ]
