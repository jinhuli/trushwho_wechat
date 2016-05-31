# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': '\u610f\u89c1\u53cd\u9988', 'verbose_name_plural': '\u610f\u89c1\u53cd\u9988'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='ftype',
            field=models.SmallIntegerField(default=b'0', verbose_name='\u53cd\u9988\u7c7b\u578b', choices=[(0, '\u95ee\u9898\u53cd\u9988'), (1, '\u63a8\u8350\u5927V'), (2, '\u5176\u4ed6')]),
        ),
    ]
