# Generated by Django 3.2.12 on 2022-03-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0002_alter_affiliates_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliates',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
