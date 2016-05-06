# coding: utf-8
'''
Created on 2016年5月6日

@author: likun
'''
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='subscribe/subscribe.html'), name='subscribe'),
]
