# coding: utf-8
'''
Created on 2016年5月4日

@author: likun
'''
from django.conf.urls import url
from django.views.decorators.cache import cache_page
from articles.views import ArticleIndexView, ArticleListView, ArticleDetailView\
, ArticleListForBigvView, ArticleJsonDataForTitleView

urlpatterns = (
    url(r'^list/$', ArticleIndexView.as_view(), name='article_index'),
    url(r'^list/(?P<token>\w+)/$', cache_page(1)(ArticleListView.as_view()), name='article_list'),
    url(r'^article_jsondata_for_title/$', ArticleJsonDataForTitleView.as_view(), name='article_jsondata_for_title'),
    url(r'^(?P<pk>[\w-]+)/$', ArticleDetailView.as_view(), name='article_item'),
    url(r'^bigv/list/(?P<v_id>[\w-]+)/$', cache_page(60)(ArticleListForBigvView.as_view()), name='article_bigv_list'),
)
