# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_delete_vine'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='namefood')),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Wine name')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='WineCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='namewine')),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.FoodCategory'),
        ),
        migrations.AddField(
            model_name='wine',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.WineCategory'),
        ),
    ]
