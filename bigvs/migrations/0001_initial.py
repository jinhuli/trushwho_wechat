# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigVs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v_id', models.CharField(max_length=36, null=True, blank=True)),
                ('name', models.CharField(max_length=32, null=True, blank=True)),
                ('da_v_type', models.IntegerField(null=True, blank=True)),
                ('belong_to', models.IntegerField(null=True, blank=True)),
                ('synonym', models.TextField(null=True, blank=True)),
                ('isdefault', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'big_vs',
                'managed': False,
            },
        ),
    ]
