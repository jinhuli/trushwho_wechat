# coding: utf-8

from common.views import WeChatView
from bigvs.models import BigVs
from wechat.models import WechatUser_BigVs, WechatUser
from django.views.generic.list import ListView
from django.http.response import JsonResponse

from common.utils import debug


class BigVsIndexView(WeChatView):
    template_name = 'bigvs/bigvs_index.html'


class BigVsListView(ListView):
    model = BigVs
    paginate_by = 20
    allow_empty = True
    
    def get_queryset(self):
        queryset = super(BigVsListView, self).get_queryset().filter(isdefault=0)
        token = self.kwargs.get('token', '')
        data = self.request.GET.copy()
        openid = data.get('openid', '')
        q = data.get('q', '')
        if q:
            queryset = queryset.filter(name__icontains=q)
        self.follows_bigvs = map(lambda x: x['bigvs_id'], WechatUser_BigVs.objects.filter(wechatuser__openid=openid).values('bigvs_id'))
        if token == 'mine':
            queryset = queryset.filter(pk__in=self.follows_bigvs)
        queryset = queryset.extra(
                select={'brief'\
                : 'select brief from big_vs_src where big_vs_src.v_id = big_vs.v_id limit 1'\
                , 'words_weight'\
                : 'select words_weight from big_vs_src where big_vs_src.v_id = big_vs.v_id limit 1'}
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        context_data = super(BigVsListView, self).get_context_data(**kwargs)
        context_data.update({'follows_bigvs': self.follows_bigvs})
        return context_data
    
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
