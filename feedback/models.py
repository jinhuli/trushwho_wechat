# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _

from wechat.models import WechatUser

class FeedBack(models.Model):
    wechatuser = models.ForeignKey(WechatUser, verbose_name=_(u'微信用户'))
    email = models.EmailField(_(u'邮箱'), null=True, blank=True)
    phone_number = models.CharField(_(u'手机'), max_length=11, null=True, blank=True)
    content = models.TextField(_(u'内容'))
    
    class Meta:
        verbose_name = verbose_name_plural = _(u'意见反馈')
        
    def __unicode__(self):
        return self.wechatuser.nickname