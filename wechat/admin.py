# coding: utf-8
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.conf.urls import url
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.admin import SimpleListFilter

from wechat.models import WechatUser, WechatUser_BigVs, Menu, Comment
from wxsdk.models import WXSdk

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


class MenuParentFilter(SimpleListFilter):
    title = _(u'父级菜单')
    parameter_name = 'parent'
    
    def lookups(self, request, model_admin):
        return [('true', _(u'是')), ('false', _(u'否'))]
    
    def queryset(self, request, queryset):
        if self.value() == 'true':
            queryset = queryset.filter(parent__isnull=True)
        elif self.value() == 'false':
            queryset = queryset.filter(parent__isnull=False)
        return queryset
    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'key', 'url', 'num')
    search_fields = ('name',)
    list_filter = (MenuParentFilter,)

    def get_urls(self):
        urls = super(MenuAdmin, self).get_urls()
        myurls = [
            url(r'^menu_create/$', self.admin_site.admin_view(self.menu_create)),
            url(r'^menu_delete/$', self.admin_site.admin_view(self.menu_delete)),
        ]
        return myurls + urls

    def menu_create(self, request):
        sdk = WXSdk()
        menus = Menu.objects.filter(parent__isnull=True, status=1)
        buttons = []
        for menu in menus:
            btn = {'name':menu.name, 'type':menu.type, 'key': menu.key, 'url':menu.url, 'media_id':menu.media_id}
            sub_menus = Menu.objects.filter(parent__id=menu.id)
            if sub_menus:
                sub_button = []
                for sub_menu in sub_menus:
                    sub_btn = {'name':sub_menu.name, 'type':sub_menu.type, 'key': sub_menu.key, 'url':sub_menu.url, 'media_id':sub_menu.media_id}
                    sub_button.append(sub_btn)
                btn.update({'sub_button':sub_button})
            buttons.append(btn)
        code, msg = sdk.menu_create(buttons)
        if code == 0:
            messages.success(request, _(u'自定义菜单创建成功！'))
        else:
            messages.error(request, _(u'自定义菜单创建失败！code:{0}, msg:{1}'.format(code, msg)))
        return redirect('admin:wechat_menu_changelist')

    def menu_delete(self, request):
        sdk = WXSdk()
        code, msg = sdk.menu_delete()
        if code == 0:
            messages.success(request, _(u'自定义菜单删除成功！'))
        else:
            messages.error(request, _(u'自定义菜单删除失败！code:{0}, msg:{1}'.format(code, msg)))
        return redirect('admin:wechat_menu_changelist')
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'parent':
            kwargs['queryset'] = Menu.objects.filter(parent__isnull=True, status=1)
        
        return super(MenuAdmin, self).formfield_for_foreignkey(db_field, request=None, **kwargs)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['wechatuser', 'content_object', 'content', 'created_datetime']
    list_filter = ['is_delete']
    search_fields = ['wechatuser__name', 'wechatuser__openid']
    raw_id_fields = ['wechatuser', 'parent']
    
