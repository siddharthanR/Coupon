# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-11-06 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='referalany',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='register',
            name='referalcode',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]
