# coding: utf-8
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from bigvs.models import BigVs
from prediction.models import PredictionBigvs

@admin.register(BigVs)
class BigVsAdmin(admin.ModelAdmin):
    list_display = ['v_id', 'name', 'words_weight', 'brief', 'da_v_type', 'belong_to', 'synonym', 'isdefault']
    list_filter = ['isdefault']
    search_fields = ['v_id', 'name']
    actions = ['select_bigv_to_prediction', ]
    
    def select_bigv_to_prediction(self, request, queryset):
        bigvs = []
        for bigv in queryset:
            if not PredictionBigvs.objects.filter(bigv=bigv).exists():
                bigvs.append(PredictionBigvs(bigv=bigv))
        PredictionBigvs.objects.bulk_create(bigvs)
        
    select_bigv_to_prediction.short_description = _(u'添加到多空看板大V选择列表')
