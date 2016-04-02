# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to='cms.CMSPlugin')),
                ('blog', models.ForeignKey(related_name='plugins', to='blog.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
