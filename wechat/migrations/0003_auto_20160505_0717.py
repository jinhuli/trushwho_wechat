# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_auto_20160429_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wechatuser_bigvs',
            name='subscribe_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 5, 7, 17, 39, 603788, tzinfo=utc), verbose_name='\u5173\u6ce8\u65f6\u95f4', auto_now_add=True),
            preserve_default=False,
        ),
    ]
