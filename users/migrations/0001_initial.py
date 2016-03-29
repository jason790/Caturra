# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('picture', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=140)),
                ('gender', models.CharField(max_length=6)),
                ('birth', models.DateTimeField(verbose_name='date birth')),
                ('subscription', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
