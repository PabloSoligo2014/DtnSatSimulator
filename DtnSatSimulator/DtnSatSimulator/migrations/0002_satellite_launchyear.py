# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DtnSatSimulator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='launchYear',
            field=models.IntegerField(default=17, verbose_name='Ano de lanzamiento, dos ultimos digitos, necesarios para crear TLE'),
        ),
    ]
