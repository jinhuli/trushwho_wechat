# coding: utf-8
'''
Created on 2016年5月5日

@author: likun
'''
from django import forms

from feedback.models import FeedBack

class FeedBackForm(forms.ModelForm):
    model = FeedBack
    
    
