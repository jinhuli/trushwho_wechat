# coding: utf-8
'''
Created on 2016年4月29日

@author: likun
'''
from django.conf.urls import url
from django.views.decorators.cache import cache_page
from bigvs.views import BigVsListView, BigVsIndexView, follow, unfollow, \
    BigvDetailView

urlpatterns = [
    url(r'^list/$', BigVsIndexView.as_view(), name='bigvs_index'),
    url(r'^list/(?P<token>\w+)/$', cache_page(60 * 60)(BigVsListView.as_view()), name='bigvs_list'),
    url(r'^wechat/follow/$', follow, name='follow'),
    url(r'^wechat/unfollow/$', unfollow, name='unfollow'),
    url(r'^(?P<v_id>[\w-]+)/$', BigvDetailView.as_view(), name='bigvs_detail'),
]

