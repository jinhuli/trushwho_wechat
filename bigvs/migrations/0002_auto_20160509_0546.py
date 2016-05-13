# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigvs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BigVsDBV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v_id', models.CharField(max_length=36, null=True, verbose_name='id', blank=True)),
                ('name', models.CharField(max_length=32, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('da_v_type', models.IntegerField(blank=True, null=True, verbose_name='\u7c7b\u578b', choices=[(1, '\u4e2a\u4eba'), (2, '\u8bc1\u5238'), (3, 'NGO')])),
                ('belong_to', models.IntegerField(null=True, verbose_name='\u673a\u6784', blank=True)),
                ('synonym', models.TextField(null=True, verbose_name='\u540c\u4e49\u8bcd', blank=True)),
                ('pinyin', models.CharField(max_length=256, null=True, verbose_name='\u62fc\u97f3', blank=True)),
                ('brief', models.TextField(null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('words_weight', models.IntegerField(null=True, verbose_name='\u8a00\u503c', blank=True)),
            ],
            options={
                'verbose_name': '\u5927V',
                'db_table': 'view_big_vs',
                'managed': False,
                'verbose_name_plural': '\u5927V',
            },
        ),
        migrations.CreateModel(
            name='BigVsSrc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v_id', models.CharField(max_length=36, verbose_name='vid')),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('nickname', models.CharField(max_length=64, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('category', models.CharField(max_length=36, null=True, verbose_name='\u5206\u7c7b', blank=True)),
                ('gender', models.CharField(max_length=6, null=True, verbose_name='\u6027\u522b', blank=True)),
                ('brief', models.TextField(null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('url', models.CharField(max_length=256, null=True, verbose_name='\u4e3b\u9875', blank=True)),
                ('fans_count', models.IntegerField(null=True, verbose_name='\u7c89\u4e1d\u6570', blank=True)),
                ('follows_count', models.IntegerField(null=True, verbose_name='\u5173\u6ce8\u6570', blank=True)),
                ('content_count', models.IntegerField(null=True, verbose_name='\u8bc4\u8bba\u6570', blank=True)),
                ('words_weight', models.IntegerField(null=True, verbose_name='\u8a00\u503c', blank=True)),
                ('related_weight', models.IntegerField(null=True, verbose_name='\u76f8\u5173\u5ea6', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u5927V',
                'db_table': 'big_vs_src',
                'managed': False,
                'verbose_name_plural': '\u5927V',
            },
        ),
        migrations.AlterModelOptions(
            name='bigvs',
            options={'managed': False, 'verbose_name': '\u5927V', 'verbose_name_plural': '\u5927V'},
        ),
    ]
