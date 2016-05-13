# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePostedResults',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, verbose_name='id', primary_key=True)),
                ('href', models.CharField(max_length=255, null=True, verbose_name='\u539f\u6587\u94fe\u63a5', blank=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u5185\u5bb9', blank=True)),
                ('publish_date', models.DateTimeField(null=True, verbose_name='\u53d1\u5e03\u65e5\u671f', blank=True)),
                ('v_id', models.CharField(max_length=36, null=True, verbose_name='\u5927Vid', blank=True)),
                ('source_id', models.CharField(max_length=36, null=True, verbose_name='\u6e90id', blank=True)),
                ('scrapy_date', models.DateTimeField(null=True, verbose_name='\u6dfb\u52a0\u65e5\u671f', blank=True)),
                ('article_type', models.CharField(max_length=2, null=True, verbose_name='\u7c7b\u578b', blank=True)),
                ('article_category', models.IntegerField(blank=True, null=True, verbose_name='\u5206\u7c7b', choices=[(1, '\u65b0\u95fb'), (2, '\u535a\u5ba2'), (3, '\u7814\u62a5')])),
                ('is_predictable', models.IntegerField(null=True, verbose_name='\u662f\u5426\u9884\u6d4b', blank=True)),
                ('summary', models.TextField(null=True, verbose_name='\u6982\u8981', blank=True)),
                ('list_of_object', models.CharField(max_length=36, null=True, blank=True)),
                ('list_of_v', models.CharField(max_length=255, null=True, blank=True)),
                ('object_keyword_title', models.CharField(max_length=255, null=True, verbose_name='\u5173\u952e\u5b57\u6807\u9898', blank=True)),
                ('object_keyword_content', models.CharField(max_length=255, null=True, verbose_name='\u5173\u952e\u5b57\u5185\u5bb9', blank=True)),
                ('other_keyword_title', models.CharField(max_length=255, null=True, verbose_name='\u5176\u4ed6\u5173\u952e\u5b57\u6807\u9898', blank=True)),
                ('other_keyword_content', models.CharField(max_length=255, null=True, verbose_name='\u5176\u4ed6\u5173\u952e\u5b57\u5185\u5bb9', blank=True)),
                ('organization_id', models.CharField(max_length=45, null=True, blank=True)),
                ('article_source', models.CharField(max_length=45, null=True, verbose_name='\u6765\u6e90', blank=True)),
                ('article_uuid', models.CharField(max_length=45, null=True, blank=True)),
                ('is_correct', models.IntegerField(blank=True, null=True, verbose_name='\u662f\u5426\u6b63\u786e', choices=[(-1, '\u5f85\u5904\u7406'), (0, '\u9519\u8bef'), (1, '\u6b63\u786e'), (2, '\u672a\u5230\u671f'), (3, '\u975e\u9884\u6d4b'), (4, '\u653e\u5f03\u5224\u65ad')])),
                ('emotion_level', models.IntegerField(blank=True, null=True, verbose_name='\u7b49\u7ea7', choices=[(1, '\u975e\u5e38\u4e50\u89c2'), (2, '\u4e50\u89c2'), (3, '\u4e2d\u6027'), (4, '\u60b2\u89c2'), (5, '\u975e\u5e38\u60b2\u89c2')])),
                ('period', models.IntegerField(blank=True, null=True, verbose_name='\u5468\u671f', choices=[(1, '\u5929'), (2, '\u5468'), (3, '\u6708'), (4, '\u5b63\u5ea6'), (5, '\u5e74'), (6, '\u4e00\u5e74\u4ee5\u4e0a')])),
                ('article_status', models.IntegerField(blank=True, null=True, verbose_name='\u72b6\u6001', choices=[(-2, '\u975e\u62bd\u6837'), (1, '\u521d\u59cb\uff08\u7b49\u5f85\u4eba\u5de5\u5904\u7406\uff09'), (2, '\u5df2\u4eba\u5de5\u5904\u7406'), (3, '\u5df2\u53d1\u9001'), (4, '\u9057\u5f03')])),
                ('comment', models.CharField(max_length=45, null=True, verbose_name='\u63cf\u8ff0', blank=True)),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': '\u6587\u7ae0',
                'db_table': 'article_posted_results',
                'managed': False,
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='ArticlesBigVsDBV',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, verbose_name='id', primary_key=True)),
                ('href', models.CharField(max_length=255, null=True, verbose_name='\u539f\u6587\u94fe\u63a5', blank=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u5185\u5bb9', blank=True)),
                ('publish_date', models.DateTimeField(null=True, verbose_name='\u53d1\u5e03\u65e5\u671f', blank=True)),
                ('v_id', models.CharField(max_length=36, null=True, verbose_name='\u5927Vid', blank=True)),
                ('source_id', models.CharField(max_length=36, null=True, verbose_name='\u6e90id', blank=True)),
                ('scrapy_date', models.DateTimeField(null=True, verbose_name='\u6dfb\u52a0\u65e5\u671f', blank=True)),
                ('article_type', models.CharField(max_length=2, null=True, verbose_name='\u7c7b\u578b', blank=True)),
                ('article_category', models.IntegerField(blank=True, null=True, verbose_name='\u5206\u7c7b', choices=[(1, '\u65b0\u95fb'), (2, '\u535a\u5ba2'), (3, '\u7814\u62a5')])),
                ('is_predictable', models.IntegerField(null=True, verbose_name='\u662f\u5426\u9884\u6d4b', blank=True)),
                ('summary', models.TextField(null=True, verbose_name='\u6982\u8981', blank=True)),
                ('list_of_object', models.CharField(max_length=36, null=True, blank=True)),
                ('list_of_v', models.CharField(max_length=255, null=True, blank=True)),
                ('object_keyword_title', models.CharField(max_length=255, null=True, verbose_name='\u5173\u952e\u5b57\u6807\u9898', blank=True)),
                ('object_keyword_content', models.CharField(max_length=255, null=True, verbose_name='\u5173\u952e\u5b57\u5185\u5bb9', blank=True)),
                ('other_keyword_title', models.CharField(max_length=255, null=True, verbose_name='\u5176\u4ed6\u5173\u952e\u5b57\u6807\u9898', blank=True)),
                ('other_keyword_content', models.CharField(max_length=255, null=True, verbose_name='\u5176\u4ed6\u5173\u952e\u5b57\u5185\u5bb9', blank=True)),
                ('organization_id', models.CharField(max_length=45, null=True, blank=True)),
                ('article_source', models.CharField(max_length=45, null=True, verbose_name='\u6765\u6e90', blank=True)),
                ('article_uuid', models.CharField(max_length=45, null=True, blank=True)),
                ('is_correct', models.IntegerField(blank=True, null=True, verbose_name='\u662f\u5426\u6b63\u786e', choices=[(-1, '\u5f85\u5904\u7406'), (0, '\u9519\u8bef'), (1, '\u6b63\u786e'), (2, '\u672a\u5230\u671f'), (3, '\u975e\u9884\u6d4b'), (4, '\u653e\u5f03\u5224\u65ad')])),
                ('emotion_level', models.IntegerField(blank=True, null=True, verbose_name='\u7b49\u7ea7', choices=[(1, '\u975e\u5e38\u4e50\u89c2'), (2, '\u4e50\u89c2'), (3, '\u4e2d\u6027'), (4, '\u60b2\u89c2'), (5, '\u975e\u5e38\u60b2\u89c2')])),
                ('period', models.IntegerField(blank=True, null=True, verbose_name='\u5468\u671f', choices=[(1, '\u5929'), (2, '\u5468'), (3, '\u6708'), (4, '\u5b63\u5ea6'), (5, '\u5e74'), (6, '\u4e00\u5e74\u4ee5\u4e0a')])),
                ('article_status', models.IntegerField(blank=True, null=True, verbose_name='\u72b6\u6001', choices=[(-2, '\u975e\u62bd\u6837'), (1, '\u521d\u59cb\uff08\u7b49\u5f85\u4eba\u5de5\u5904\u7406\uff09'), (2, '\u5df2\u4eba\u5de5\u5904\u7406'), (3, '\u5df2\u53d1\u9001'), (4, '\u9057\u5f03')])),
                ('comment', models.CharField(max_length=45, null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('bigv_name', models.CharField(max_length=32, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('bigv_pinyin', models.CharField(max_length=256, null=True, verbose_name='\u62fc\u97f3', blank=True)),
                ('bigv_brief', models.TextField(null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('bigv_words_weight', models.IntegerField(null=True, verbose_name='\u8a00\u503c', blank=True)),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': '\u6587\u7ae0',
                'db_table': 'view_articles_bigvs',
                'managed': False,
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
