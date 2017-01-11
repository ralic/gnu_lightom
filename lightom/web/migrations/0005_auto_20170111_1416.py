# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170111_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='programar',
            name='nome',
            field=models.CharField(default=django.utils.timezone.now, help_text='Nome da programação', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='concentrador',
            name='latitude',
            field=models.CharField(help_text='Coordenada de latitude', max_length=100),
        ),
        migrations.AlterField(
            model_name='concentrador',
            name='longitude',
            field=models.CharField(help_text='Coordenada de longitude', max_length=100),
        ),
        migrations.AlterField(
            model_name='concentrador',
            name='serial',
            field=models.CharField(help_text='Número serial', max_length=100),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='corrente',
            field=models.PositiveIntegerField(help_text='Corrente atual'),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='estado',
            field=models.BooleanField(help_text='Estado da lâmpada'),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='fase',
            field=models.PositiveIntegerField(help_text='Fase atual'),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='latitude',
            field=models.CharField(help_text='Coordenada de latitude', max_length=100),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='longitude',
            field=models.CharField(help_text='Coordenada de longitude', max_length=100),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='serial',
            field=models.CharField(help_text='Número serial', max_length=100),
        ),
        migrations.AlterField(
            model_name='programar',
            name='fim',
            field=models.DateTimeField(help_text='Horário de término'),
        ),
        migrations.AlterField(
            model_name='suporte',
            name='usuario',
            field=models.CharField(help_text='Usuário do telegram', max_length=100, verbose_name='Usuário'),
        ),
    ]
