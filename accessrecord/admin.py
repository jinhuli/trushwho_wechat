# coding: utf-8
from django.contrib import admin
from accessrecord.models import AccessRecord

@admin.register(AccessRecord)
class AccessRecordAdmin(admin.ModelAdmin):
    list_display = ['openid', 'record', 'type', 'keyword', 'ip', 'access_time']
    search_fields = ['openid', ]

