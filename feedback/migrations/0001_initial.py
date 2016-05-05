# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0003_auto_20160505_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1', blank=True)),
                ('phone_number', models.CharField(max_length=11, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('wechatuser', models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', to='wechat.WechatUser')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u53cd\u9988',
                'verbose_name_plural': '\u7528\u6237\u53cd\u9988',
            },
        ),
    ]
