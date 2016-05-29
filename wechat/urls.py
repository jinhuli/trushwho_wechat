# coding: utf-8
'''
Created on 2016年5月18日

@author: likun
'''

from django.conf.urls import url
from wechat.views import CommentCreateView
from common.decorators import openid_exempt

urlpatterns = [
    url(r'^comment/add/$', openid_exempt(CommentCreateView.as_view()), name='comment_add'),
]
