# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigvs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WechatUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open_id', models.CharField(unique=True, max_length=45, verbose_name='openid')),
                ('nickname', models.CharField(max_length=45, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('sex', models.IntegerField(blank=True, null=True, verbose_name='\u6027\u522b', choices=[(0, '\u672a\u77e5'), (1, '\u7537'), (2, '\u5973')])),
                ('city', models.CharField(max_length=45, null=True, verbose_name='\u57ce\u5e02', blank=True)),
                ('country', models.CharField(max_length=45, null=True, verbose_name='\u56fd\u5bb6', blank=True)),
                ('province', models.CharField(max_length=45, null=True, verbose_name='\u7701\u4efd', blank=True)),
                ('language', models.CharField(max_length=45, null=True, verbose_name='\u8bed\u8a00', blank=True)),
                ('headimgurl', models.CharField(max_length=512, null=True, verbose_name='\u5934\u50cf', blank=True)),
                ('subscribe_time', models.DateTimeField(null=True, verbose_name='\u5173\u6ce8\u65f6\u95f4', blank=True)),
                ('groupid', models.IntegerField(null=True, verbose_name='\u7ec4', blank=True)),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u7528\u6237',
                'verbose_name_plural': '\u5fae\u4fe1\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='WechatUser_BigVs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscribe_time', models.DateTimeField(null=True, verbose_name='\u5173\u6ce8\u65f6\u95f4', blank=True)),
                ('bigvs', models.ForeignKey(verbose_name='\u5927V', to='bigvs.BigVs')),
                ('wechatuser', models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', to='wechat.WechatUser')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u5173\u6ce8\u5927V',
                'verbose_name_plural': '\u7528\u6237\u5173\u6ce8\u5927V',
            },
        ),
        migrations.AlterUniqueTogether(
            name='wechatuser_bigvs',
            unique_together=set([('wechatuser', 'bigvs')]),
        ),
    ]
