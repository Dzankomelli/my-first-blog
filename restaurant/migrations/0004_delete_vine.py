# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_vine'),
    ]

    operations = [
        migrations.DeleteModel(
            name='vine',
        ),
    ]
