# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0006_auto_20160520_1419'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judgement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('hint_text', models.TextField(null=True, verbose_name='\u63d0\u793a\u6587\u5b57', blank=True)),
                ('remind_date', models.DateField(null=True, verbose_name='\u63d0\u9192\u65e5\u671f', blank=True)),
                ('judge', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u5224\u65ad', choices=[(b'wrong', '\u9519\u8bef'), (b'right', '\u6b63\u786e')])),
                ('judge_datetime', models.DateTimeField(null=True, verbose_name='\u5224\u65ad\u65e5\u671f', blank=True)),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', to='articles.ArticlePostedResults')),
                ('wechatuser', models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', to='wechat.WechatUser')),
            ],
            options={
                'db_table': 'wechat_judgement',
                'verbose_name': '\u5224\u65ad',
                'verbose_name_plural': '\u5224\u65ad',
            },
        ),
        migrations.AlterUniqueTogether(
            name='judgement',
            unique_together=set([('wechatuser', 'article')]),
        ),
    ]
