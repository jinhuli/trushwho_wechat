# coding: utf-8
'''
Created on 2016年4月29日

@author: likun
'''
from django.conf.urls import url
from bigvs.views import BigVsListView, BigVsIndexView, follow, unfollow, \
    BigvDetailView, BigvJsonDataForTitleView
from common.decorators import openid_exempt


urlpatterns = [
    url(r'^list/$', BigVsIndexView.as_view(), name='bigvs_index'),
    url(r'^list/(?P<token>\w+)/$', openid_exempt(BigVsListView.as_view()), name='bigvs_list'),
    url(r'^wechat/follow/$', follow, name='follow'),
    url(r'^wechat/unfollow/$', unfollow, name='unfollow'),
    url(r'^jsondata_for_title/$', openid_exempt(BigvJsonDataForTitleView.as_view()), name='bigvs_jsondata_for_title'),
    url(r'^(?P<v_id>[\w-]+)/$', BigvDetailView.as_view(), name='bigvs_detail'),
]

