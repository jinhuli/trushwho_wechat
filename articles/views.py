# coding: utf-8

from django.views.generic.list import ListView
from django.db.models import Q
from articles.models import ArticlePostedResults
from wechat.models import WechatUser_BigVs
from common.views import WeChatView, WeChatDetailView
from bigvs.models import BigVsSrc

class ArticleIndexView(WeChatView):
    template_name = 'articles/articles_index.html'
    
    
class ArticleListView(ListView):
    model = ArticlePostedResults
    paginate_by = 20
    allow_empty = True
    template_name = 'articles/articles_list.html'
    
    def get_queryset(self):
        queryset = super(ArticleListView, self).get_queryset()
        token = self.kwargs.get('token', '')
        data = self.request.GET.copy()
        openid = data.get('openid', '')
        q = data.get('q', '')
        queryset = queryset.extra(\
                select={'bigv_name'\
                : 'select name from big_vs_src where big_vs_src.v_id = article_posted_results.v_id limit 1'\
                , 'words_weight'\
                : 'select words_weight from big_vs_src where big_vs_src.v_id = article_posted_results.v_id limit 1'}
        )
        if q:
            queryset = queryset.filter(title__icontains=q)
        
        if token == 'mine':
            follows_bigvs = [bv.bigvs.v_id for bv in WechatUser_BigVs.objects.filter(wechatuser__openid=openid)]
            queryset = queryset.filter(v_id__in=follows_bigvs)
        return queryset

class ArticleDetailView(WeChatDetailView):
    template_name = 'articles/articles_item.html'
    model = ArticlePostedResults
    context_object_name = 'obj'
    
    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object(queryset)
        bigv = BigVsSrc.objects.filter(v_id=obj.v_id)
        if bigv.exists():
            obj.bigv_name = bigv[0].name
            obj.words_weight = bigv[0].words_weight
        return obj
