# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0007_ngo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='ngo_name',
            new_name='ngo',
        ),
    ]
