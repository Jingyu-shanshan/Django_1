# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_auto_20180114_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(default=20, max_length=10),
            preserve_default=False,
        ),
    ]