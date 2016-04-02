# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('slug', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
    ]
