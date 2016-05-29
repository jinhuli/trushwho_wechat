# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('articles', '0001_initial'),
        ('wechat', '0004_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('object_id', models.CharField(max_length=36, verbose_name='id')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('delete_datetime', models.DateTimeField(null=True, verbose_name='\u5220\u9664\u65f6\u95f4', blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(verbose_name='\u697c\u4e3b', blank=True, to='wechat.Comment', null=True)),
                ('wechatuser', models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', to='wechat.WechatUser')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
