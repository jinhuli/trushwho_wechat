# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigvs', '0003_auto_20160512_1552'),
        ('prediction', '0002_auto_20160510_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionBigvs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('bigv', models.ForeignKey(verbose_name='\u5927V', to='bigvs.BigVs', unique=True)),
            ],
            options={
                'verbose_name': '\u5927V\u9009\u62e9\u5217\u8868',
                'verbose_name_plural': '\u5927V\u9009\u62e9\u5217\u8868',
            },
        ),
    ]
