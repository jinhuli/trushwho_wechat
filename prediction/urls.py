# coding: utf-8
'''
Created on 2016年5月10日

@author: likun
'''

from django.conf.urls import url
from django.views.decorators.cache import cache_page
from prediction.views import PredictionView, ArticleListForSelectView

urlpatterns = [
    url(r'^$', cache_page(60)(PredictionView.as_view()), name='prediction'),
    url(r'^article_list_for_select/$', ArticleListForSelectView.as_view(), name='article_list_for_select'),
]
