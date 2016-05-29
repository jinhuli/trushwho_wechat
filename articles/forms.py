# coding: utf-8
'''
Created on 2016年5月23日

@author: likun
'''
from django import forms
from articles.models import Judgement

class JudgementForm(forms.ModelForm):
    class Meta:
        model = Judgement
        fields = '__all__'
