# Generated by Django 3.2.12 on 2022-03-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0005_alter_investment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
