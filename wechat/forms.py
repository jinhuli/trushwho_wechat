# coding: utf-8
'''
Created on 2016年5月18日

@author: likun
'''
from django import forms

from wechat.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'