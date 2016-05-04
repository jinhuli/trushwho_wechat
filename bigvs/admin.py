# coding: utf-8
from django.contrib import admin

from bigvs.models import BigVs

@admin.register(BigVs)
class BigVsAdmin(admin.ModelAdmin):
    list_display = ['v_id', 'name', 'da_v_type', 'belong_to', 'synonym', 'isdefault']
    list_filter = ['isdefault']
    search_fields = ['v_id', 'name']
