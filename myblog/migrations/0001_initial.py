# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-28 00:25
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
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]