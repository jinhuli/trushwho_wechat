# coding: utf-8
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from articles.models import ArticlePostedResults, Judgement


@admin.register(ArticlePostedResults)
class ArticlePostedResultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'title', 'publish_date', 'scrapy_date'\
                    , 'article_source'\
                    , 'article_uuid', 'is_correct', 'article_status']
    list_filter = ['article_category', 'is_correct', 'emotion_level', 'period'\
                   , 'article_status']
    search_fields = ['bigv__v_id', 'title', 'bigv__name', ]
    raw_id_fields = ['bigv', ]
    
    def link(self, obj):
        return u'<a href="{0}" target="_blank">查看</a>'.format(obj.href)
    
    link.allow_tags = True
    link.short_description = _(u'原文链接')
    
    
    

@admin.register(Judgement)
class JudgementAdmin(admin.ModelAdmin):
    list_display = ['wechatuser', 'article', 'remind_date', 'judge', 'judge_datetime']
    list_filter = ['judge']
    search_fields = ['wechatuser__name', 'wechatuser__openid', 'article__title']
    raw_id_fields = ['article', 'wechatuser']
