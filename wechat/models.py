# coding: utf-8
'''
Created on 2016年4月28日

@author: likun
'''

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from bigvs.models import BigVs
from common.constants import WECHAT_USER_SEX_CHOICES

import datetime


class WechatUser(models.Model):
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
