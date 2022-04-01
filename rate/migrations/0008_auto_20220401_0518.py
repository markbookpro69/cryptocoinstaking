# Generated by Django 3.2.12 on 2022-04-01 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0007_rate_fake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='interest_rate',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rate',
            name='minimum_investment',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
        migrations.AlterField(
            model_name='rate',
            name='minimum_withdrawal',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
    ]