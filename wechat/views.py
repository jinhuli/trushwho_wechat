# coding: utf-8
'''
Created on 2016年4月28日

@author: likun
'''
from django.views.generic.edit import CreateView
from wechat.forms import CommentForm


class CommentCreateView(CreateView):
    form_class = CommentForm
    
    def get_success_url(self):
        return self.object.content_object.get_absolute_url()