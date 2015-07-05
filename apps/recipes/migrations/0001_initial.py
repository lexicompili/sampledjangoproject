# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.FileField(upload_to=b'')),
                ('ingredients', models.TextField()),
                ('method', models.TextField()),
                ('cooktime', models.IntegerField()),
                ('fat', models.FloatField()),
                ('carbs', models.FloatField()),
                ('protein', models.FloatField()),
                ('calories', models.FloatField()),
                ('category', models.ForeignKey(to='recipes.Category')),
            ],
        ),
    ]
