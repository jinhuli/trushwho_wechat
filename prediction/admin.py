# coding: utf-8
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _

from prediction.models import Prediction, PredictionBigvs
from prediction.forms import PredictionForm
from bigvs.models import BigVs
from articles.models import ArticlePostedResults

from datetime import datetime


class CurrentTimeListFilter(SimpleListFilter):
    title = _(u'当前时间有效')
    parameter_name = 'ct'
    
    def lookups(self, request, model_admin):
        return [('yes', _(u'是')), ('no', _(u'否')), ]
    
    def queryset(self, request, queryset):
        if self.value() == 'yes':
            queryset = queryset.filter(start_datetime__lte=datetime.now(), end_datetime__gte=datetime.now())
        elif self.value() == 'no':
            queryset = queryset.exclude(start_datetime__lte=datetime.now(), end_datetime__gte=datetime.now())
        return queryset
    

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['bigv', 'article', 'viewpoint', 'start_datetime', 'end_datetime']
    search_fields = ['bigv__name', 'bigv__v_id']
    list_filter = ['viewpoint', CurrentTimeListFilter]
    raw_id_fields = ['article', ]
    form = PredictionForm
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        data = PredictionBigvs.objects.select_related().values('bigv__v_id')
        vids = map(lambda x: x['bigv__v_id'], data)
        if db_field.name == 'bigv':
            kwargs['queryset'] = BigVs.objects.filter(v_id__in=vids).only('id', 'name')
        if db_field.name == 'article':
            kwargs['queryset'] = ArticlePostedResults.active_objects.filter(bigv_id__in=vids).only('id', 'title')
        
        return super(PredictionAdmin, self).formfield_for_foreignkey(db_field, request=None, **kwargs)


@admin.register(PredictionBigvs)
class PredictionBigvsAdmin(admin.ModelAdmin):
    list_display = ['bigv', 'created_datetime']
    search_fields = ['bigv__name', 'bigv__v_id']
    raw_id_fields = ['bigv', ]
