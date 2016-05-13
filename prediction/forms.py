# coding: utf-8
'''
Created on 2016年5月12日

@author: likun
'''
from django import forms
from django.utils.translation import gettext_lazy as _

from prediction.models import Prediction

class NoValidateChoiceField(forms.ChoiceField):
    def valid_value(self, value):
        return True

class PredictionForm(forms.ModelForm):
    article_select = NoValidateChoiceField(label=_('文章列表'))
    
    class Meta:
        model = Prediction
        fields = ['bigv', 'article_select', 'article', 'viewpoint', 'start_datetime', 'end_datetime'] 