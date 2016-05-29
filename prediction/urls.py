# coding: utf-8
'''
Created on 2016年5月10日

@author: likun
'''

from django.conf.urls import url
from django.conf import settings
from django.views.decorators.cache import cache_page
from prediction.views import PredictionView, ArticleListForSelectView
from common.decorators import openid_exempt


urlpatterns = [
    url(r'^$', cache_page(settings.SITE_REDIS_TIMEOUT)(PredictionView.as_view()), name='prediction'),
    url(r'^article_list_for_select/$', openid_exempt(ArticleListForSelectView.as_view()), name='article_list_for_select'),
]
