# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('dob', models.DateField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
