# coding: utf-8
'''
Created on 2016年5月4日

@author: likun
'''
from django.conf.urls import url
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from articles.views import ArticleIndexView, ArticleListView, ArticleDetailView\
, ArticleListForBigvView, ArticleJsonDataForTitleView, JudgementView, JudgementCreateView\
, JudgementDeleteView, MineJudgementListView
from common.decorators import openid_exempt


urlpatterns = (
    url(r'^list/$', ArticleIndexView.as_view(), name='article_index'),
    url(r'^judge/$', openid_exempt(JudgementView.as_view()), name='article_judge'),
    url(r'^judge/add/$', openid_exempt(JudgementCreateView.as_view()), name='article_judge_add'),
    url(r'^judge/delete/$', csrf_exempt(openid_exempt(JudgementDeleteView.as_view())), name='article_judge_delete'),
    url(r'^list/judge/$', cache_page(1)(openid_exempt(MineJudgementListView.as_view())), name='article_judge_list'),
    url(r'^list/(?P<token>\w+)/$', cache_page(1)(openid_exempt(ArticleListView.as_view())), name='article_list'),
    url(r'^article_jsondata_for_title/$', openid_exempt(ArticleJsonDataForTitleView.as_view()), name='article_jsondata_for_title'),
    url(r'^(?P<pk>[\w-]+)/$', ArticleDetailView.as_view(), name='article_item'),
    url(r'^bigv/list/(?P<v_id>[\w-]+)/$', cache_page(1)(openid_exempt(ArticleListForBigvView.as_view())), name='article_bigv_list'),
    
)
