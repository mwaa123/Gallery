# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-19 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0003_auto_20200520_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]