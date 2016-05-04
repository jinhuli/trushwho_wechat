# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.constants import ARTICLE_CATEGORY_CHOICES, ARTICLE_IS_CORRECT_CHOICES\
, ARTICLE_EMOTION_LEVEL_CHOICES, ARTICLE_PERIOD_CHOICES, ARTICLE_STATUS_CHOICES


class ArticlePostedResults(models.Model):
    id = models.CharField(_(u'id'), primary_key=True, max_length=36)
    href = models.CharField(_(u'原文链接'), max_length=255, blank=True, null=True)
    title = models.CharField(_(u'标题'), max_length=255, blank=True, null=True)
    content = models.TextField(_(u'内容'), blank=True, null=True)
    publish_date = models.DateTimeField(_(u'发布日期'), blank=True, null=True)
    v_id = models.CharField(_(u'大Vid'), max_length=36, blank=True, null=True)
    source_id = models.CharField(_(u'源id'), max_length=36, blank=True, null=True)
    scrapy_date = models.DateTimeField(_(u'添加日期'), blank=True, null=True)
    article_type = models.CharField(_(u'类型'), max_length=2, blank=True, null=True)
    article_category = models.IntegerField(_(u'分类'), blank=True, null=True, choices=ARTICLE_CATEGORY_CHOICES)
    is_predictable = models.IntegerField(_(u'是否预测'), blank=True, null=True)
    summary = models.TextField(_(u'概要'), blank=True, null=True)
    list_of_object = models.CharField(max_length=36, blank=True, null=True)
    list_of_v = models.CharField(max_length=255, blank=True, null=True)
    object_keyword_title = models.CharField(_(u'关键字标题'), max_length=255, blank=True, null=True)
    object_keyword_content = models.CharField(_(u'关键字内容'), max_length=255, blank=True, null=True)
    other_keyword_title = models.CharField(_(u'其他关键字标题'), max_length=255, blank=True, null=True)
    other_keyword_content = models.CharField(_(u'其他关键字内容'), max_length=255, blank=True, null=True)
    organization_id = models.CharField(max_length=45, blank=True, null=True)
    article_source = models.CharField(_(u'来源'), max_length=45, blank=True, null=True)
    article_uuid = models.CharField(max_length=45, blank=True, null=True)
    is_correct = models.IntegerField(_(u'是否正确'), blank=True, null=True, choices=ARTICLE_IS_CORRECT_CHOICES)
    emotion_level = models.IntegerField(_(u'等级'), blank=True, null=True, choices=ARTICLE_EMOTION_LEVEL_CHOICES)
    period = models.IntegerField(_(u'周期'), blank=True, null=True, choices=ARTICLE_PERIOD_CHOICES)
    article_status = models.IntegerField(_(u'状态'), blank=True, null=True, choices=ARTICLE_STATUS_CHOICES)
    comment = models.CharField(_(u'描述'), max_length=45, blank=True, null=True)
 
    class Meta:
        managed = False
        db_table = 'article_posted_results'
        verbose_name = verbose_name_plural = _(u'文章')
        ordering = ('-publish_date',)
        
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('article_item', None, {'pk': self.id})
