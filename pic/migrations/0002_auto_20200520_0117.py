# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-19 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(max_length=30),
        ),
    ]