# Generated by Django 3.2.6 on 2021-08-21 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210821_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Премьера в мире'),
        ),
    ]
