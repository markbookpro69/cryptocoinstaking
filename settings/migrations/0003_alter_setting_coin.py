# Generated by Django 3.2.12 on 2022-03-07 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20220307_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='coin',
            field=models.ForeignKey(default='USDT', on_delete=django.db.models.deletion.CASCADE, to='settings.coin', verbose_name='Coin'),
        ),
    ]
