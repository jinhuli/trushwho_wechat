# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0006_auto_20160520_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='wechatuser',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 31, 8, 31, 8, 88504, tzinfo=utc), verbose_name='\u521b\u5efa\u65f6\u95f4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wechatuser',
            name='modified_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 31, 8, 31, 17, 269441, tzinfo=utc), verbose_name='\u4fee\u6539\u65f6\u95f4', auto_now=True),
            preserve_default=False,
        ),
    ]
