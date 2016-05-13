# coding: utf-8
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from wechat.models import WechatUser, WechatUser_BigVs
# Register your models here.

@admin.register(WechatUser)
class WechatUserAdmin(admin.ModelAdmin):
    list_display = ['openid', 'nickname', 'sex', 'city', 'province', 'country', 'language', 'headimg'\
                    , 'subscribe_time', 'groupid']
    list_filter = ['sex', 'city', 'province', 'country']
    search_fields = ['openid', 'nickname']
    
    def headimg(self, obj):
        return u'<a href="{0}" target="_blank"><img src="{0}" title="{1}" width="40"/></a>'\
            .format(obj.headimgurl, obj.nickname)
    
    headimg.allow_tags = True
    headimg.short_description = _(u'头像')
    
@admin.register(WechatUser_BigVs)
class WechatUser_BigVsAdmin(admin.ModelAdmin):
    list_display = ['wechatuser', 'bigvs', 'subscribe_time']
    search_fields = ['wechatuser__openid', 'wechatuser__nickname', 'bigvs__name']
    raw_id_fields = ['bigvs', 'wechatuser']
