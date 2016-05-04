# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wechatuser_bigvs',
            options={'verbose_name': '\u5173\u6ce8\u5927V', 'verbose_name_plural': '\u5173\u6ce8\u5927V'},
        ),
        migrations.RenameField(
            model_name='wechatuser',
            old_name='open_id',
            new_name='openid',
        ),
    ]
