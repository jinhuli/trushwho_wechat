# coding: utf-8
from django.contrib import admin

from articles.models import ArticlePostedResults


@admin.register(ArticlePostedResults)
class ArticlePostedResultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'href', 'title', 'publish_date', 'v_id', 'source_id', 'scrapy_date'\
                    , 'article_type', 'article_category', 'is_predictable', 'summary', 'article_source'\
                    , 'article_uuid', 'is_correct', 'emotion_level', 'period', 'article_status']
    
    list_filter = ['article_category', 'article_source', 'is_correct', 'emotion_level', 'period'\
                   , 'article_status']
    
    search_fields = ['v_id', 'title']
    
