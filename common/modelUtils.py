    # coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.constants import STATUS_CHOICES

class TimestampMixin(models.Model):
    created_datetime = models.DateTimeField(_(u'创建时间'), auto_now_add=True)
    modified_datetime = models.DateTimeField(_(u'修改时间'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-modified_datetime',)

class StatusMixin(models.Model):
    status = models.PositiveIntegerField(_(u'状态'), choices=STATUS_CHOICES)
    class Meta:
        abstract = True
        ordering = ('status',)
