# Generated by Django 3.2.12 on 2022-03-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0003_alter_investment_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investment',
            options={'ordering': ['date_created']},
        ),
    ]
