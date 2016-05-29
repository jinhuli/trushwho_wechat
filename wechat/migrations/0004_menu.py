# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0003_auto_20160505_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.PositiveIntegerField(verbose_name='\u72b6\u6001', choices=[(0, '\u65e0\u6548'), (1, '\u6709\u6548')])),
                ('num', models.IntegerField(default=1, help_text='\u6309\u6b64\u5e8f\u53f7\u4ece\u5c0f\u5230\u5927\u6392\u5e8f', verbose_name='\u5e8f\u53f7')),
                ('name', models.CharField(help_text='\u4e0d\u8d85\u8fc716\u4e2a\u5b57\u8282\uff0c\u5b50\u83dc\u5355\u4e0d\u8d85\u8fc740\u4e2a\u5b57\u8282', max_length=40, verbose_name='\u83dc\u5355\u6807\u9898')),
                ('type', models.CharField(max_length=256, verbose_name='\u83dc\u5355\u7684\u54cd\u5e94\u52a8\u4f5c\u7c7b\u578b', choices=[(b'click', '\u70b9\u51fb\u63a8\u4e8b\u4ef6'), (b'view', '\u8df3\u8f6cURL'), (b'scancode_push', '\u626b\u7801\u63a8\u4e8b\u4ef6'), (b'scancode_waitmsg', '\u626b\u7801\u63a8\u4e8b\u4ef6\u4e14\u5f39\u51fa\u201c\u6d88\u606f\u63a5\u6536\u4e2d\u201d\u63d0\u793a\u6846'), (b'pic_sysphoto', '\u5f39\u51fa\u7cfb\u7edf\u62cd\u7167\u53d1\u56fe'), (b'pic_photo_or_album', '\u5f39\u51fa\u62cd\u7167\u6216\u8005\u76f8\u518c\u53d1\u56fe'), (b'pic_weixin', '\u5f39\u51fa\u5fae\u4fe1\u76f8\u518c\u53d1\u56fe\u5668'), (b'location_select', '\u5f39\u51fa\u5730\u7406\u4f4d\u7f6e\u9009\u62e9\u5668'), (b'media_id', '\u4e0b\u53d1\u6d88\u606f\uff08\u9664\u6587\u672c\u6d88\u606f\uff09'), (b'view_limited', '\u8df3\u8f6c\u56fe\u6587\u6d88\u606fURL')])),
                ('key', models.CharField(help_text='click\u7b49\u70b9\u51fb\u7c7b\u578b\u5fc5\u987b\u3002\u83dc\u5355KEY\u503c\uff0c\u7528\u4e8e\u6d88\u606f\u63a5\u53e3\u63a8\u9001\uff0c\u4e0d\u8d85\u8fc7128\u5b57\u8282', max_length=128, null=True, verbose_name='KEY', blank=True)),
                ('url', models.URLField(help_text='\u7f51\u9875\u94fe\u63a5\uff0c\u7528\u6237\u70b9\u51fb\u83dc\u5355\u53ef\u6253\u5f00\u94fe\u63a5\uff0c\u4e0d\u8d85\u8fc7256\u5b57\u8282', max_length=256, null=True, verbose_name='\u8df3\u8f6curl', blank=True)),
                ('media_id', models.CharField(help_text='\u8c03\u7528\u65b0\u589e\u6c38\u4e45\u7d20\u6750\u63a5\u53e3\u8fd4\u56de\u7684\u5408\u6cd5media_id', max_length=256, null=True, verbose_name='media_id', blank=True)),
                ('parent', models.ForeignKey(blank=True, to='wechat.Menu', help_text='\u4e00\u7ea7\u83dc\u5355\u6570\u5e94\u4e3a1~3\u4e2a,\u4e8c\u7ea7\u83dc\u5355\u4e2a\u6570\u5e94\u4e3a1~5\u4e2a', null=True, verbose_name='\u7236\u7ea7\u83dc\u5355')),
            ],
            options={
                'ordering': ('num',),
                'verbose_name': '\u83dc\u5355',
                'verbose_name_plural': '\u83dc\u5355',
            },
        ),
    ]
