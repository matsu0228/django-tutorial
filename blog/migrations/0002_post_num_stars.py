# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_stars',
            field=models.IntegerField(default=0),
        ),
    ]
