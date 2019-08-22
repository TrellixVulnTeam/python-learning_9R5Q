# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-21 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media/')),
                ('body', models.TextField()),
            ],
        ),
    ]
