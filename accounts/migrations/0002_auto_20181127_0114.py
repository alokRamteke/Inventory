# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='remark',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='material',
            name='remark',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
