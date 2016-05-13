# coding: utf-8
from django.contrib import admin

from prediction.models import Prediction, PredictionBigvs
from prediction.forms import PredictionForm
from bigvs.models import BigVs
from articles.models import ArticlePostedResults

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['bigv', 'article', 'viewpoint', 'start_datetime', 'end_datetime']
    search_fields = ['bigv__name', 'bigv__v_id']
    list_filter = ['viewpoint']
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
