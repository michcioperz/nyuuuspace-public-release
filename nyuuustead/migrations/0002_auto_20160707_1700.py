# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-07 17:00
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations
import nyuuustead.models


class Migration(migrations.Migration):

    dependencies = [
        ('nyuuustead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userware',
            name='colour',
            field=colorful.fields.RGBColorField(colors=['#1b85b8', '#03c03c', '#559e83', '#ae5a41', '#c3cb71', '#c23b22', '#ffb347', '#f49ac2', '#dea5a4', '#e3e387', '#77dd77', '#b19cd9', '#ffd1dc', '#779ecb', '#cb99c9', '#966fd6'], default=nyuuustead.models.best_colour),
        ),
    ]
