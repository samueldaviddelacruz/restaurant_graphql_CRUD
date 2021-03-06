# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True, null=True)),
                ('CreatedAt', models.DateTimeField(verbose_name='Category Creation date')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Description', models.TextField(blank=True, null=True)),
                ('Price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantapi.Category')),
            ],
        ),
    ]
