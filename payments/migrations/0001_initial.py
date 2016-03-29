# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('last_digits', models.CharField(max_length=4)),
                ('gateway', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('amount', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
