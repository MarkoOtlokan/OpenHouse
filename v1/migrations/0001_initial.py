# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Rasperrypi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=32)),
                ('code', models.TextField()),
                ('password', models.CharField(max_length=32)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.House')),
            ],
        ),
        migrations.CreateModel(
            name='TerminalRasperrypi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=32)),
                ('code', models.TextField()),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='housenetwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.HouseNetwork'),
        ),
        migrations.AddField(
            model_name='house',
            name='terminalrasperrypi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.TerminalRasperrypi'),
        ),
    ]