# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_company_number',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
