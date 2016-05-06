# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _

class AccessRecord(models.Model):
    openid = models.CharField(_(u'openid'), max_length=45)
    record = models.CharField(_(u'url'), max_length=512)
    access_time = models.DateTimeField(_(u'访问时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = verbose_name_plural = _(u'访问记录')
        
