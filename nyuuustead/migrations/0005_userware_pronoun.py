# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-07 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nyuuustead', '0004_auto_20160707_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='userware',
            name='pronoun',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='pronouns', to='nyuuustead.Pronoun'),
            preserve_default=False,
        ),
    ]
