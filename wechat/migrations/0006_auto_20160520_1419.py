# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0005_auto_20160517_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u5220\u9664'),
        ),
    ]
