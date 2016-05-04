# coding: utf-8
'''
Created on 2016年5月4日

@author: likun
'''
from django.conf.urls import url
from articles.views import ArticleIndexView, ArticleListView, ArticleDetailView

urlpatterns = (
    url(r'^list/$', ArticleIndexView.as_view(), name='article_index'),
    url(r'^list/(?P<token>\w+)/$', ArticleListView.as_view(), name='article_list'),
    url(r'^item/(?P<pk>\w+)/$', ArticleDetailView.as_view(), name='article_item'),
)