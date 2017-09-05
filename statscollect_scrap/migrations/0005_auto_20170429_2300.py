# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statscollect_scrap', '0004_auto_20170429_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedgamerating',
            name='footballperson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='statscollect_db.FootballPerson'),
        ),
        migrations.AlterField(
            model_name='processedgamesheetplayer',
            name='footballperson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='statscollect_db.FootballPerson'),
        ),
    ]
