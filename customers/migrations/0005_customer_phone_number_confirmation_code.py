# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20161231_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number_confirmation_code',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
