# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.constants import ACCESSRECORD_TYPE_CHOICES

class AccessRecord(models.Model):
    openid = models.CharField(_(u'openid'), max_length=45)
    record = models.CharField(_(u'url'), max_length=512)
    ip = models.GenericIPAddressField(_(u'ip'), null=True, blank=True)
    keyword = models.CharField(_(u'搜索关键字'), max_length=512, null=True, blank=True)
    type = models.CharField(_(u'类别'), choices=ACCESSRECORD_TYPE_CHOICES, max_length=32, null=True, blank=True, db_index=True)
    access_time = models.DateTimeField(_(u'访问时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = verbose_name_plural = _(u'访问记录')
        
