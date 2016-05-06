# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=45, verbose_name='openid')),
                ('record', models.CharField(max_length=512, verbose_name='url')),
                ('access_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8bbf\u95ee\u65f6\u95f4')),
            ],
        ),
    ]
