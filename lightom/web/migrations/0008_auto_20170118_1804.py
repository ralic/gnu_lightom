# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170111_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concentrador',
            name='serial',
            field=models.CharField(help_text='Número serial', max_length=50, primary_key=True, serialize=False),
        ),
    ]