# Generated by Django 3.2.12 on 2022-03-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_coin_coin_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='alfacoins_id',
            field=models.CharField(default='bitcoin', max_length=12),
            preserve_default=False,
        ),
    ]
