# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _

from bigvs.models import BigVs
from articles.models import ArticlePostedResults
from common.constants import PREDICTION_VIEWPOINT_CHOICES

class Prediction(models.Model):
    bigv = models.ForeignKey(BigVs, verbose_name=_(u'大V'))
    article = models.ForeignKey(ArticlePostedResults, verbose_name=_(u'文章'))
    viewpoint = models.CharField(_(u'观点'), max_length=16, choices=PREDICTION_VIEWPOINT_CHOICES)
    start_datetime = models.DateTimeField(_(u'开始时间'))
    end_datetime = models.DateTimeField(_(u'结束时间'))
    
    class Meta:
        verbose_name = verbose_name_plural = _(u'多空看板')
        unique_together = ('bigv', 'article')
        
    def __unicode__(self):
        return self.bigv.name
    
class PredictionBigvs(models.Model):
    bigv = models.ForeignKey(BigVs, verbose_name=_(u'大V'), unique=True)
    created_datetime = models.DateTimeField(_(u'创建时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = verbose_name_plural = _(u'大V选择列表')
