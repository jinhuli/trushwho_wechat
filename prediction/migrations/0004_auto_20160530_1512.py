# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0006_auto_20160520_1419'),
        ('prediction', '0003_predictionbigvs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('wechatuser', models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', to='wechat.WechatUser', unique=True)),
            ],
            options={
                'verbose_name': '\u8ba2\u9605\u7528\u6237',
                'verbose_name_plural': '\u8ba2\u9605\u7528\u6237',
            },
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together=set([('bigv', 'article')]),
        ),
    ]
