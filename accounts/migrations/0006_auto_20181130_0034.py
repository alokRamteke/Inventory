# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-29 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_material_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=15)),
                ('Remarks', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='material',
            name='account',
        ),
        migrations.RemoveField(
            model_name='material',
            name='quantity',
        ),
        migrations.AddField(
            model_name='account',
            name='Remark',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='maerial_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Material'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='Remarks',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customers'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
