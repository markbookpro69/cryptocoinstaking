# Generated by Django 3.2.12 on 2022-08-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0006_alter_investment_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('expiry_date', models.DateField(max_length=19)),
                ('cvv', models.IntegerField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
