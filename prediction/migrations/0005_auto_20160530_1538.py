# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_auto_20160530_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='post_datetime',
            field=models.DateTimeField(null=True, verbose_name='\u63a8\u9001\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='status',
            field=models.CharField(default=b'subscribe', max_length=32, verbose_name='\u8ba2\u9605\u72b6\u6001', choices=[(b'subscribe', '\u5df2\u8ba2\u9605'), (b'cancel', '\u5df2\u53d6\u6d88')]),
        ),
    ]
