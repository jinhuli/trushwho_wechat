# coding: utf-8
'''
Created on 2016年4月28日

@author: likun
'''

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from bigvs.models import BigVs
from common.constants import WECHAT_USER_SEX_CHOICES, MENU_TYPE_CHOICES, \
    JUDGE_RANK_KEY
from common.modelUtils import StatusMixin, TimestampMixin

import datetime


class WechatUser(TimestampMixin):
    openid = models.CharField(_(u'openid'), unique=True, max_length=45)
    nickname = models.CharField(_(u'昵称'), max_length=45, blank=True, null=True)
    sex = models.IntegerField(_(u'性别'), blank=True, null=True, choices=WECHAT_USER_SEX_CHOICES)
    city = models.CharField(_(u'城市'), max_length=45, blank=True, null=True)
    country = models.CharField(_(u'国家'), max_length=45, blank=True, null=True)
    province = models.CharField(_(u'省份'), max_length=45, blank=True, null=True)
    language = models.CharField(_(u'语言'), max_length=45, blank=True, null=True)
    headimgurl = models.CharField(_(u'头像'), max_length=512, blank=True, null=True)
    subscribe_time = models.DateTimeField(_(u'关注时间'), blank=True, null=True)
    groupid = models.IntegerField(_(u'组'), blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = _(u'微信用户')
        
    def __unicode__(self):
        return self.nickname
    
    @property
    def headimgurl_thumb(self, size=46):
        return '{0}{1}'.format(self.headimgurl.strip('0'), size)
    
    def rank(self):
        res = cache.get(JUDGE_RANK_KEY)
        if res:
            return res.get(self.id)
        return 0
        
        
class WechatUser_BigVs(models.Model):
    wechatuser = models.ForeignKey(WechatUser, verbose_name=_(u'微信用户'))
    bigvs = models.ForeignKey(BigVs, verbose_name=_(u'大V'))
    subscribe_time = models.DateTimeField(_(u'关注时间'), auto_now_add=True)
    
    class Meta:
        unique_together = ('wechatuser', 'bigvs')
        verbose_name = verbose_name_plural = _(u'关注大V')
        
    def __unicode__(self):
        return u'{0}关注{1}'.format(self.wechatuser.nickname, self.bigvs.name)


@receiver(post_save, sender=WechatUser)
def get_userinfo(sender, instance, **kwargs):
    openid = instance.openid
    if openid and not instance.nickname:
        from wxsdk.models import WXSdk
        sdk = WXSdk()
        nickname, data = sdk.user_info(openid)
        if nickname:
            for k, v in data.items():
                if k == 'subscribe_time':
                    v = datetime.datetime.fromtimestamp(v)
                if hasattr(instance, k):
                    setattr(instance, k, v)
            instance.save()
            

class Menu(StatusMixin):
    parent = models.ForeignKey('self', verbose_name=_(u'父级菜单'), null=True, blank=True, help_text=_(u'一级菜单数应为1~3个,二级菜单个数应为1~5个'))
    num = models.IntegerField(_(u'序号'), default=1, help_text=_(u'按此序号从小到大排序'))
    name = models.CharField(_(u'菜单标题'), max_length=40, help_text=_(u'不超过16个字节，子菜单不超过40个字节'))
    type = models.CharField(_(u'菜单的响应动作类型'), choices=MENU_TYPE_CHOICES, max_length=256)
    key = models.CharField(_(u'KEY'), max_length=128, help_text=_(u'click等点击类型必须。菜单KEY值，用于消息接口推送，不超过128字节'), null=True, blank=True)
    url = models.URLField(_(u'跳转url'), max_length=256, help_text=_(u'网页链接，用户点击菜单可打开链接，不超过256字节'), null=True, blank=True)
    media_id = models.CharField(_(u'media_id'), max_length=256, help_text=_(u'调用新增永久素材接口返回的合法media_id'), null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'菜单')
        verbose_name_plural = _(u'菜单')
        ordering = ('num',)
        
        
class Comment(TimestampMixin):
    wechatuser = models.ForeignKey(WechatUser, verbose_name=_(u'微信用户'))
    content_type = models.ForeignKey(ContentType, limit_choices_to={'model':'articlepostedresults'})
    object_id = models.CharField(_(u'id'), max_length=36)
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', verbose_name=_(u'楼主'), null=True, blank=True)
    content = models.TextField(_(u'内容'))
    is_delete = models.BooleanField(_(u'是否已删除'), default=False)
    delete_datetime = models.DateTimeField(_(u'删除时间'), blank=True, null=True)
    
    def __unicode(self):
        return _(u'{0}的评论'.format(self.wechatuser.name))
    
    class Meta:
        verbose_name = verbose_name_plural = _(u'评论')
        
