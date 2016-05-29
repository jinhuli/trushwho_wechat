# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessrecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessrecord',
            options={'verbose_name': '\u8bbf\u95ee\u8bb0\u5f55', 'verbose_name_plural': '\u8bbf\u95ee\u8bb0\u5f55'},
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='ip',
            field=models.GenericIPAddressField(null=True, verbose_name='ip', blank=True),
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='keyword',
            field=models.CharField(max_length=512, null=True, verbose_name='\u641c\u7d22\u5173\u952e\u5b57', blank=True),
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='type',
            field=models.CharField(choices=[(b'articles', '\u6587\u7ae0'), (b'bigvs', '\u5927V'), (b'feedback', '\u53cd\u9988'), (b'subscribe', '\u8ba2\u9605'), (b'prediction', '\u591a\u7a7a\u770b\u677f'), (b'user', '\u7528\u6237\u64cd\u4f5c')], max_length=32, blank=True, null=True, verbose_name='\u7c7b\u522b', db_index=True),
        ),
    ]
