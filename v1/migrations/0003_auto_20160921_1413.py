# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_auto_20160920_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.FileField(upload_to=b'')),
                ('command', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='terminalrasperrypi',
            name='code',
            field=models.FileField(upload_to='veljko'),
        ),
        migrations.AddField(
            model_name='function',
            name='Trasperrypi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='v1.TerminalRasperrypi'),
        ),
        migrations.AddField(
            model_name='function',
            name='rasperrypi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='v1.Rasperrypi'),
        ),
    ]
