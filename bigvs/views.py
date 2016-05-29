# coding: utf-8
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http.response import JsonResponse
from django.db.models import Q

from common.views import WeChatView, JSONListView
from bigvs.models import BigVs
from wechat.models import WechatUser_BigVs, WechatUser
from common.utils import debug
from common.decorators import openid_exempt
from articles.models import ArticlePostedResults


class BigVsIndexView(WeChatView):
    template_name = 'bigvs/bigvs_index.html'


class BigVsListView(ListView):
    model = BigVs
    paginate_by = 20
    allow_empty = False
    template_name = 'bigvs/bigvs_list.html'
    
    def get_queryset(self):
        queryset = super(BigVsListView, self).get_queryset()
        token = self.kwargs.get('token', '')
        data = self.request.GET.copy()
        openid = data.get('openid', '')
        q = data.get('q', '')
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(pinyin__icontains=q))
        bigvs_ids = WechatUser_BigVs.objects.filter(wechatuser__openid=openid).values('bigvs_id')
        self.follows_bigvs = map(lambda x: x['bigvs_id'], bigvs_ids)
        if token == 'mine':
            queryset = queryset.filter(pk__in=self.follows_bigvs)
        
        return queryset.only('v_id', 'name', 'brief', 'words_weight')
    
    def get_context_data(self, **kwargs):
        context_data = super(BigVsListView, self).get_context_data(**kwargs)
        context_data.update({'follows_bigvs': self.follows_bigvs})
        context_data.update({'token': self.kwargs.get('token', 'all')})
        return context_data


@openid_exempt
def follow(request):
    data = request.GET.copy()
    openid = data.get('openid')
    bigv_id = data.get('bigv_id')
    try:
        WechatUser_BigVs.objects.create(wechatuser=WechatUser.objects.get(openid=openid)\
                                        , bigvs=BigVs.objects.get(pk=bigv_id))
    except Exception as e:
        debug('follow', e, True)
        return JsonResponse({"res": False})
    return JsonResponse({"res": True})


@openid_exempt
def unfollow(request):
    data = request.GET.copy()
    openid = data.get('openid')
    bigv_id = data.get('bigv_id')
    try:
        WechatUser_BigVs.objects.filter(wechatuser__openid=openid, bigvs__id=bigv_id).delete()
    except Exception as e:
        debug('unfollow', e, True)
        return JsonResponse({"res": False})
    return JsonResponse({"res": True})


class BigvDetailView(DetailView):
    template_name = 'bigvs/bigvs_detail.html'
    context_object_name = 'obj'
    model = BigVs
    slug_field = 'v_id'
    slug_url_kwarg = 'v_id'
    
    def get_queryset(self):
        return super(BigvDetailView, self).get_queryset().only('name', 'v_id', 'brief', 'words_weight')
    
    def get_context_data(self, **kwargs):
        context = super(BigvDetailView, self).get_context_data(**kwargs)
        obj = kwargs.get('object')
        followers = WechatUser_BigVs.objects.filter(bigvs_id=obj.id).count()
        is_follow = WechatUser_BigVs.objects.filter(wechatuser=self.request.wechatuser, bigvs_id=obj.id)
        articles = ArticlePostedResults.objects.filter(bigv_id=obj.v_id).count()
        context.update({'followers': followers, 'articles': articles, 'is_follow':is_follow})
        return context
    
    
class BigvJsonDataForTitleView(JSONListView):
    model = BigVs
    
    def get_queryset(self):
        queryset = super(BigvJsonDataForTitleView, self).get_queryset()
        data = self.request.GET.copy()
        q = data.get('keyword', '')
        openid = data.get('openid', '')
        token = data.get('token', '')
        queryset = queryset.filter(Q(name__icontains=q) | Q(pinyin__icontains=q))
        if token == 'mine':
            bigvs_ids = WechatUser_BigVs.objects.filter(wechatuser__openid=openid).values('bigvs_id')
            follows_bigvs = map(lambda x: x['bigvs_id'], bigvs_ids)
            queryset = queryset.filter(pk__in=follows_bigvs)
        queryset = queryset.only('name', 'pinyin')[:10]
        return queryset
    
    def get_data(self, context):
        queryset = self.get_queryset()
        res = []
        for x in queryset:
            res.append({'label': x.name, 'value': x.pinyin})
            res.append({'label': x.name, 'value': x.name})
        return res

