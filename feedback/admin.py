# coding: utf-8
from django.contrib import admin

from feedback.models import FeedBack

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['wechatuser', 'email', 'phone_number', 'content']
    search_fields = ['wecharuser__nickname', ]
