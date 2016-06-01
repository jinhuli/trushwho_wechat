# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import striptags
from django.core.cache import cache

from common.constants import ARTICLE_CATEGORY_CHOICES, ARTICLE_IS_CORRECT_CHOICES\
, ARTICLE_EMOTION_LEVEL_CHOICES, ARTICLE_PERIOD_CHOICES, ARTICLE_STATUS_CHOICES, JUDGEMENT_JUDGE_CHOICES, \
    ARTICLE_COMMENTS_KEY, ARTICLE_JUDGEMENT_RIGHT_KEY, \
    ARTICLE_JUDGEMENT_WRONG_KEY, ARTICLE_IS_JUDGEMENT_CHOICES, \
    ARTICLE_JUDGEMENT_CALENDAR_KEY, BIGVS_ALL_KEY
from bigvs.models import BigVs
from common.modelUtils import TimestampMixin
from wechat.models import WechatUser, Comment
from django.contrib.contenttypes.fields import GenericRelation


class ArticleActiveManager(models.Manager):
    def get_queryset(self):
        return super(ArticleActiveManager, self).get_queryset().filter(article_status__in=(-2, 2, 3))


class ArticlePostedResults(models.Model):
    id = models.CharField(_(u'id'), primary_key=True, max_length=36)
    href = models.CharField(_(u'原文链接'), max_length=255, blank=True, null=True)
    title = models.CharField(_(u'标题'), max_length=255, blank=True, null=True)
    content = models.TextField(_(u'内容'), blank=True, null=True)
    publish_date = models.DateTimeField(_(u'发布日期'), blank=True, null=True)
    bigv = models.ForeignKey(BigVs, to_field='v_id', verbose_name=_(u'大Vid'), max_length=36, db_column='v_id')
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
    score = models.DecimalField(_(u'分数'), max_digits=5, decimal_places=2)
    is_judgement = models.IntegerField(_(u'是否判断'), blank=True, null=True, choices=ARTICLE_IS_JUDGEMENT_CHOICES)
    objects = models.Manager()
    active_objects = ArticleActiveManager()
    comments = GenericRelation(Comment, related_query_name='articles')
    
    class Meta:
        managed = False
        db_table = 'article_posted_results'
        verbose_name = verbose_name_plural = _(u'文章')
        ordering = ('-publish_date',)
        
    def __unicode__(self):
        return self.title and self.title or striptags(self.content)[:40]
    
    @models.permalink
    def get_absolute_url(self):
        return ('article_item', None, {'pk': self.id})
    
    def bigv_dict(self):
        res = cache.get(BIGVS_ALL_KEY)
        if res is None:
            return self.bigv
        return res.get(self.bigv_id)
    
    def comments_count(self):
        res = cache.get(ARTICLE_COMMENTS_KEY)
        if res is None:
            return self.comments.count()
        return res.get(self.id, '')
    
    def judgement_right(self):
        res = cache.get(ARTICLE_JUDGEMENT_RIGHT_KEY)
        if res is None:
            return self.judgement_set.filter(judge='right').count()
        count = res.get(self.id)
        z = self.is_correct == 1 and 1 or 0
        if count:
            return  count + z
        else:
            return z and z or ''
    
    def judgement_wrong(self):
        res = cache.get(ARTICLE_JUDGEMENT_WRONG_KEY)
        if res is None:
            return self.judgement_set.filter(judge='wrong').count()
        count = res.get(self.id)
        z = self.is_correct == 0 and 1 or 0
        if count:
            return  count + z
        else:
            return z and z or ''
    
    def judgement_calendar(self):
        res = cache.get(ARTICLE_JUDGEMENT_CALENDAR_KEY)
        if res is None:
            return self.judgement_set.filter(judge__isnull=True).count()
        count = res.get(self.id, '')
        if count:
            return u'<b>{0}</b>人加入日历'.format(count)
        return count


class Judgement(TimestampMixin):
    wechatuser = models.ForeignKey(WechatUser, verbose_name=_(u'微信用户'))
    hint_text = models.TextField(_(u'提示文字'), null=True, blank=True)
    remind_date = models.DateField(_(u'提醒日期'), null=True, blank=True)
    judge = models.CharField(_(u'判断'), max_length=16, choices=JUDGEMENT_JUDGE_CHOICES, null=True, blank=True)
    judge_datetime = models.DateTimeField(_(u'判断日期'), null=True, blank=True)
    article = models.ForeignKey(ArticlePostedResults, verbose_name=_(u'文章'))
    
    def __unicode(self):
        return _(u'{0}对{1}的判断'.format(self.wechatuser.name, self.article.title))
    
    class Meta:
        verbose_name = verbose_name_plural = _(u'判断')
        unique_together = ('wechatuser', 'article')
        db_table = 'wechat_judgement'

