# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='established',
            field=models.DateField(),
        ),
    ]