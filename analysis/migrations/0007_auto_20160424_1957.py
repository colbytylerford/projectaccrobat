# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_auto_20160424_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to='MAFfiles/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='output',
            field=models.TextField(null=True),
        ),
    ]
