# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170111_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concentrador',
            options={'verbose_name': 'Concentrador', 'verbose_name_plural': 'Concentradores'},
        ),
        migrations.AlterModelOptions(
            name='dispositivo',
            options={'verbose_name': 'Dispositivo', 'verbose_name_plural': 'Dispositivos'},
        ),
        migrations.AlterModelOptions(
            name='programardimerizacao',
            options={'verbose_name': 'Programar Dismerização', 'verbose_name_plural': 'Programar Dismerizações'},
        ),
        migrations.AlterModelOptions(
            name='programarestado',
            options={'verbose_name': 'Programar Estado', 'verbose_name_plural': 'Programar Estados'},
        ),
        migrations.AlterModelOptions(
            name='suporte',
            options={'verbose_name': 'Suporte', 'verbose_name_plural': 'Suportes'},
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='dimerizacao',
            field=models.PositiveSmallIntegerField(help_text='Nível de dimerização', verbose_name='Dimerização'),
        ),
    ]
