# coding: utf-8
'''
Created on 2016年5月12日

@author: likun
'''
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db.models import Q

from prediction.models import Prediction

class NoValidateChoiceField(forms.ChoiceField):
    def valid_value(self, value):
        return True

class PredictionForm(forms.ModelForm):
    article_select = NoValidateChoiceField(label=_('文章列表'), required=False)
    
    class Meta:
        model = Prediction
        fields = ['bigv', 'article_select', 'article', 'viewpoint', 'start_datetime', 'end_datetime'] 
        
    def clean(self):
        start_datetime = self.cleaned_data['start_datetime']
        end_datetime = self.cleaned_data['end_datetime']
        if start_datetime > end_datetime:
            self.add_error('end_datetime', ValidationError(_(u'结束时间不能小于开始时间。')))
        if not self.instance.pk:
            bigv = self.cleaned_data['bigv']
            
            if Prediction.objects.filter(bigv=bigv).exclude(Q(start_datetime__gt=end_datetime)\
                                            | Q(end_datetime__lt=start_datetime)).exists():
                self.add_error('bigv', ValidationError(_(u'一个大V同一时间区间只能有一个观点。')))
        return self.cleaned_data
    
