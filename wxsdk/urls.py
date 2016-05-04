# coding: utf-8
'''
Created on 2016年4月28日

@author: likun
'''


from django.conf.urls import url, patterns

urlpatterns = patterns('wxsdk.views',
    url('wx_config/$', 'wx_config', name='jssdk_wx_config'),
    url('escape/$', 'escape', name='jssdk_wx_escape'),
)
