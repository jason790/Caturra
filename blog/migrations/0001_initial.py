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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
