# coding: utf-8
from django.db.models.aggregates import Count
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet
from django.views.decorators.csrf import csrf_exempt
from prediction.models import Prediction, Subscribe
from common.constants import PREDICTION_VIEWPOINT_CHOICES
from articles.models import ArticlePostedResults
from articles.utils import cache_options, cache_bigv
from datetime import datetime
from django.http.response import JsonResponse
from common.utils import debug
from common.decorators import openid_exempt
from wechat.models import WechatUser


class PredictionView(ListView):
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
            'article__bigv_id', 'article__title', 'article__content', 'article__publish_date'\
            , 'article__article_source', 'bigv__name', 'bigv__words_weight', 'article__is_correct').order_by('-article__publish_date')})
        
        context_data.update({'data': data})
        object_list = context_data.get('object_list').only('article__id', 'bigv__v_id')
        cache_options(map(lambda x: x.article.id, object_list), self.request.wechatuser.openid)
        v_ids = list(set(map(lambda x: x.bigv.v_id, object_list)))
        cache_bigv(v_ids)
        is_subscribe = Subscribe.objects.filter(wechatuser=self.request.wechatuser, status='subscribe').exists()
        context_data.update({'is_subscribe': is_subscribe})
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


@csrf_exempt
@openid_exempt
def subscribe(request):
    openid = request.session['openid']
    try:
        sub = Subscribe.objects.get(wechatuser__openid=openid)
        sub.status = 'subscribe'
        sub.save()
    except Subscribe.DoesNotExist:
        Subscribe.objects.create(wechatuser=WechatUser.objects.get(openid=openid), status='subscribe')
    except Exception as e:
        debug('subscribe', e)
        return JsonResponse({'res':'error'})
    return JsonResponse({'res':'ok'})


@csrf_exempt
@openid_exempt
def unsubscribe(request):
    openid = request.session['openid']
    try:
        Subscribe.objects.filter(wechatuser__openid=openid, status='subscribe').update(status='cancel')
    except Exception as e:
        debug('unsubscribe', e)
        return JsonResponse({'res':'error'})
    return JsonResponse({'res':'ok'})
    
