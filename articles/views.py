# coding: utf-8

from django.views.generic.list import ListView
from django.db.models import Q, F, ExpressionWrapper, Func
from django.db.models.fields import FloatField
from articles.models import ArticlePostedResults
from wechat.models import WechatUser_BigVs
from common.views import WeChatView, WeChatDetailView, JSONListView
import time


class ArticleIndexView(WeChatView):
    template_name = 'articles/articles_index.html'
    
    
class ArticleListView(ListView):
    model = ArticlePostedResults
    paginate_by = 20
    allow_empty = True
    template_name = 'articles/articles_list.html'
    
    def get_queryset(self):
        queryset = ArticlePostedResults.active_objects.select_related()
        token = self.kwargs.get('token', '')
        data = self.request.GET.copy()
        openid = data.get('openid', '')
        q = data.get('q', '')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(bigv__name__icontains=q) | Q(bigv__pinyin__icontains=q))
        
        if token == 'mine':
            mine = WechatUser_BigVs.objects.select_related().filter(wechatuser__openid=openid).only('bigvs__v_id')
            follows_bigvs = [bv.bigvs.v_id for bv in mine]
            queryset = queryset.filter(bigv__v_id__in=follows_bigvs)
        last = time.mktime(queryset.only('publish_date').latest('publish_date').publish_date.timetuple())
#         queryset = queryset.annotate(level=ExpressionWrapper((2000 - ((last - Func(F('publish_date'), function='UNIX_TIMESTAMP')) / 60.0)) * 0.05 + F('bigv__words_weight'), output_field=FloatField()))\
#             .order_by('-level')
        queryset = queryset.extra(select={
                            'level': '(((2000 - (({0} - UNIX_TIMESTAMP(publish_date)) / 60)) * 0.05) + words_weight)'.format(last),
                            }).order_by('-level')
        return queryset.only('bigv_id', 'title', 'content', 'bigv__name', 'bigv__words_weight', 'publish_date', 'article_source')


class ArticleDetailView(WeChatDetailView):
    template_name = 'articles/articles_item.html'
    model = ArticlePostedResults
    context_object_name = 'obj'
    
    def get_queryset(self):
        return ArticlePostedResults.active_objects.select_related().only('bigv_id', 'title', 'content', 'publish_date', 'article_source', 'bigv__name', 'bigv__words_weight')


class ArticleListForBigvView(ListView):
    model = ArticlePostedResults
    paginate_by = 20
    allow_empty = True
    template_name = 'articles/articles_for_bigv_list.html'
    
    def get_queryset(self):
        queryset = ArticlePostedResults.active_objects.select_related()
        v_id = self.kwargs.get('v_id', '')
        queryset = queryset.filter(bigv__v_id=v_id).only('title', 'content', 'publish_date')
        return queryset
    

class ArticleJsonDataForTitleView(JSONListView):
    model = ArticlePostedResults
    
    def get_queryset(self):
        queryset = ArticlePostedResults.active_objects.select_related()
        data = self.request.GET.copy()
        q = data.get('keyword', '')
        openid = data.get('openid', '')
        token = data.get('token', '')
        queryset = queryset.filter(title__isnull=False).filter(Q(title__icontains=q) | Q(bigv__pinyin__icontains=q) | Q(bigv__name__icontains=q))
        if token == 'mine':
            mine = WechatUser_BigVs.objects.select_related().filter(wechatuser__openid=openid).only('bigvs__v_id')
            follows_bigvs = [bv.bigvs.v_id for bv in mine]
            queryset = queryset.filter(bigv__v_id__in=follows_bigvs)
        
        queryset = queryset.only('bigv__name', 'bigv__pinyin', 'title')[:10]
        return queryset
    
    def get_data(self, context):
        qs = self.get_queryset()
        res = []
        for x in qs:
            res.append({'label': x.title, 'value': x.bigv.pinyin})
            res.append({'label': x.title, 'value': x.bigv.name})
            res.append({'label': x.title, 'value': x.title})
        return res
    
