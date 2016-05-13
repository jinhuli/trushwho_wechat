# coding: utf-8
from django.db.models.aggregates import Count

from common.views import WeChatListView
from prediction.models import Prediction

from datetime import datetime
from common.constants import PREDICTION_VIEWPOINT_CHOICES
from articles.models import ArticlePostedResults
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet


class PredictionView(WeChatListView):
    model = Prediction
    template_name = 'prediction/index.html'
    
    def get_queryset(self):
        queryset = Prediction.objects.select_related().filter(start_datetime__lte=datetime.now(), end_datetime__gte=datetime.now())
        return queryset
    
    def get_context_data(self, **kwargs):
        context_data = super(PredictionView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        data = queryset.values('viewpoint').annotate(value=Count('viewpoint'))
        for d in data:
            d.update({'name': dict(PREDICTION_VIEWPOINT_CHOICES)[d['viewpoint']].title()})
            d.update({'items': queryset.filter(viewpoint=d['viewpoint']).only(\
            'bigv__v_id', 'article__title', 'article__content', 'article__publish_date'\
            , 'article__article_source', 'bigv__name', 'bigv__words_weight').order_by('-article__publish_date')})
        
        context_data.update({'data': data})
        return context_data
    

class ArticleListForSelectView(ListView):
    model = ArticlePostedResults
    template_name = 'prediction/article_list_for_select.html'
    
    def get_queryset(self):
        data = self.request.GET.copy()
        bid = data.get('id', '')
        if bid:
            queryset = ArticlePostedResults.active_objects.filter(bigv__id=bid).only('id', 'title').order_by('-publish_date')[:10]
            return queryset
        return EmptyQuerySet
    
    
