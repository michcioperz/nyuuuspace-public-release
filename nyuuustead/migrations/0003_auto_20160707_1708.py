# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-07 17:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nyuuustead', '0002_auto_20160707_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userware',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userware', to=settings.AUTH_USER_MODEL),
        ),
    ]
