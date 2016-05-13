# coding: utf-8
from django.utils.translation import gettext_lazy as _
from django.db import models

from common.constants import BIGVS_DA_V_TYPE_CHOICES, BIGVS_IS_DEFAULT_CHOICES

# Create your models here.

class BigVs(models.Model):
    v_id = models.CharField(_(u'id'), max_length=36, unique=True)
    name = models.CharField(_(u'名称'), max_length=32, blank=True, null=True)
    da_v_type = models.IntegerField(_(u'类型'), blank=True, null=True, choices=BIGVS_DA_V_TYPE_CHOICES)
    belong_to = models.IntegerField(_(u'机构'), blank=True, null=True)
    synonym = models.TextField(_(u'同义词'), blank=True, null=True)
    pinyin = models.CharField(_(u'拼音'), max_length=256, blank=True, null=True)
    isdefault = models.IntegerField(_(u'名称类型'), blank=True, null=True, choices=BIGVS_IS_DEFAULT_CHOICES)
    words_weight = models.IntegerField(_(u'言值'), blank=True, null=True)
    brief = models.TextField(_(u'简介'), blank=True, null=True)
 
    class Meta:
        managed = False
        db_table = 'big_vs'
        verbose_name = verbose_name_plural = _(u'大V')
        ordering = ('-words_weight',)
    
    def __unicode__(self):
        return self.name
        
class BigVsSrc(models.Model):
    v_id = models.CharField(_(u'vid'), max_length=36)
    name = models.CharField(_(u'名称'), max_length=64)
    nickname = models.CharField(_(u'昵称'), max_length=64, blank=True, null=True)
    category = models.CharField(_(u'分类'), max_length=36, blank=True, null=True)
    gender = models.CharField(_(u'性别'), max_length=6, blank=True, null=True)
    brief = models.TextField(_(u'简介'), blank=True, null=True)
    url = models.CharField(_(u'主页'), max_length=256, blank=True, null=True)
    fans_count = models.IntegerField(_(u'粉丝数'), blank=True, null=True)
    follows_count = models.IntegerField(_(u'关注数'), blank=True, null=True)
    content_count = models.IntegerField(_(u'评论数'), blank=True, null=True)
    words_weight = models.IntegerField(_(u'言值'), blank=True, null=True)
    related_weight = models.IntegerField(_(u'相关度'), blank=True, null=True)
    comment = models.TextField(_(u'备注'), blank=True, null=True)
 
    class Meta:
        managed = False
        db_table = 'big_vs_src'
        verbose_name = verbose_name_plural = _(u'大V')
        
    def __unicode__(self):
        return '{0}--{1}'.format(self.name, self.category)

    
def build_pinyin_for_name():
    from xpinyin import Pinyin
    p = Pinyin()
    for bv in BigVs.objects.filter(isdefault=0):
        if bv.name and not bv.pinyin:
            bv.pinyin = p.get_pinyin(bv.name, u'')
            bv.save()
            print bv.name + "----" + bv.pinyin


def build_brief_from_src():
    for bv in BigVsSrc.objects.filter(brief__isnull=False).exclude(brief=''):
        BigVs.objects.filter(v_id=bv.v_id).update(brief=bv.brief)
        print bv.v_id, bv.name


def build_words_weight():
    from articles.models import ArticlePostedResults
    from django.db.models.aggregates import Count
    for b in BigVs.objects.all():
        data = ArticlePostedResults.active_objects.filter(bigv__v_id=b.v_id, is_correct__in=(0, 1)).values('is_correct').annotate(count=Count('is_correct')).order_by('is_correct')
        sum , w = 0, 0
        for d in data:
            if d['is_correct'] == 1:
                c = d['count']
            sum += d['count']
        if sum:
            w = int(round(c * 1.0 / sum * 100)) 
            b.words_weight = w
            b.save()
        print b.name, w
        
