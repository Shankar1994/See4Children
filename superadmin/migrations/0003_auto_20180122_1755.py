# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_auto_20180122_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='child_code',
            new_name='child_name',
        ),
    ]
