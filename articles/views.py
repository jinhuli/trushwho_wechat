# coding: utf-8
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.contenttypes.models import ContentType
from articles.models import ArticlePostedResults, Judgement
from wechat.models import WechatUser_BigVs, WechatUser
from common.views import JSONListView, JSONView
from articles.utils import cache_options, cache_bigv, CountPaginator
from articles.forms import JudgementForm
from common.utils import debug

import datetime


class ArticleIndexView(TemplateView):
    template_name = 'articles/articles_index.html'
    
    
class ArticleListView(ListView):
    model = ArticlePostedResults
    paginate_by = 20
    allow_empty = False
    template_name = 'articles/articles_list.html'
    paginator_class = CountPaginator
    
    def get_queryset(self):
        now = datetime.datetime.now()
        queryset = ArticlePostedResults.active_objects.filter(publish_date__gt=now - datetime.timedelta(days=60))
        token = self.kwargs.get('token', '')
        data = self.request.GET.copy()
        openid = data.get('openid', '')
        q = data.get('q', '')
        if q:
            queryset = queryset.filter(title__icontains=q)
        if token == 'mine':
            mine = WechatUser_BigVs.objects.select_related().filter(wechatuser__openid=openid).only('bigvs__v_id')
            follows_bigvs = [bv.bigvs.v_id for bv in mine]
            queryset = queryset.filter(bigv__v_id__in=follows_bigvs)
        else:
            queryset = queryset.order_by('-score')

        return queryset.only('bigv_id', 'title', 'content', 'publish_date', 'article_source', 'score')
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data()
        object_list = list(context.get('object_list').only('id', 'bigv_id'))
        object_ids = map(lambda x: x.id, object_list)
        v_ids = list(set(map(lambda x: x.bigv_id, object_list)))
        cache_bigv(v_ids)
        cache_options(object_ids, self.request.session['openid'])
        return context

    
class ArticleDetailView(DetailView):
    template_name = 'articles/articles_item.html'
    model = ArticlePostedResults
    context_object_name = 'obj'
    
    def get_queryset(self):
        return ArticlePostedResults.active_objects.select_related().only('bigv_id', 'title', 'content', 'publish_date', 'article_source', 'bigv__name', 'bigv__words_weight')
    
    def get_context_data(self, **kwargs):
        content_type = ContentType.objects.get_for_model(ArticlePostedResults).id
        context_data = super(ArticleDetailView, self).get_context_data()
        context_data.update({'content_type': content_type})
        is_comments = self.object.comments.exists()
        if is_comments:
            comments = self.object.comments.select_related().only('content', 'created_datetime', 'wechatuser__nickname', 'wechatuser__headimgurl')
            context_data.update({'comments': comments})
        context_data.update({'is_comments': is_comments})
        cache_options([self.object.id], self.request.wechatuser.openid)
        return context_data
        

class ArticleListForBigvView(ListView):
    model = ArticlePostedResults
    paginate_by = 20
    allow_empty = True
    template_name = 'articles/articles_for_bigv_list.html'
    
    def get_queryset(self):
        queryset = ArticlePostedResults.active_objects
        v_id = self.kwargs.get('v_id', '')
        data = self.request.GET.copy()
        token = data.get('token')
        queryset = queryset.filter(bigv__v_id=v_id)
        if token == 'judge':
            queryset = queryset.filter(is_judgement=1)
        else:
            queryset = queryset.filter(is_judgement=0)
        return queryset.only('title', 'content', 'publish_date', 'article_source', 'score')
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListForBigvView, self).get_context_data()
        object_list = list(context.get('object_list').only('id'))
        object_ids = map(lambda x: x.id, object_list)
        cache_options(object_ids, self.request.session['openid'])
        data = self.request.GET.copy()
        token = data.get('token')
        context.update({'token': token})
        return context
    

class ArticleJsonDataForTitleView(JSONListView):
    model = ArticlePostedResults
    
    def get_queryset(self):
        queryset = ArticlePostedResults.active_objects
        data = self.request.GET.copy()
        q = data.get('keyword', '')
        openid = data.get('openid', '')
        token = data.get('token', '')
        queryset = queryset.filter(title__isnull=False).filter(title__icontains=q)
        if token == 'mine':
            mine = WechatUser_BigVs.objects.select_related().filter(wechatuser__openid=openid).only('bigvs__v_id')
            follows_bigvs = [bv.bigvs.v_id for bv in mine]
            queryset = queryset.filter(bigv__v_id__in=follows_bigvs)
        
        queryset = queryset.only('title')[:10]
        return queryset
    
    def get_data(self, context):
        qs = self.get_queryset()
        res = []
        for x in qs:
            res.append({'label': x.title, 'value': x.title})
        return res


class JudgementView(TemplateView):
    template_name = 'articles/judgement.html'

    def get_context_data(self, **kwargs):
        context_data = super(JudgementView, self).get_context_data()
        aid = self.request.GET.get('id', '')
        context_data.update({'aid': aid})
        try:
            judgement = Judgement.objects.get(wechatuser__openid=self.request.session['openid'], article__id=aid)
            context_data.update({'judgement': judgement})
        except Judgement.DoesNotExist:
            pass
        return context_data


class JudgementCreateView(JSONView):
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        openid = data.get('wechatuser')
        wechatuser = WechatUser.objects.get(openid=openid)
        data.update({'wechatuser': wechatuser.id})
        article_id = data.get('article')
        judge = data.get('judge', '')
        if judge:
            data.update({'judge_datetime': datetime.datetime.now()})
            data.update({'remind_date': datetime.datetime.now().date()})
        try:
            instance = Judgement.objects.get(wechatuser__id=wechatuser.id, article__id=article_id)
        except Judgement.DoesNotExist:
            instance = None
        form = JudgementForm(data, instance=instance)
        res = {'status': 'ok'}
        if form.is_valid():
            form.save()
            ArticlePostedResults.objects.filter(pk=article_id).update(is_judgement=1)
        else:
            debug('judgement_created', form.errors)
            res.update({'status':'error'})
        
        return self.render_to_json_response(res)


class JudgementDeleteView(JSONView):
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        pk = data.get('id', '')
        res = {'status': 'ok'}
        try:
            instance = Judgement.objects.get(pk=pk)
            instance.delete()
        except Judgement.DoesNotExist:
            res.update({'status':'error'})
        
        return self.render_to_json_response(res)


class MineJudgementListView(ListView):
    model = ArticlePostedResults
    paginate_by = 20
    allow_empty = False
    template_name = 'articles/articles_list.html'
    
    def get_queryset(self):
        now = datetime.datetime.now()
        data = self.request.GET.copy()
        jtype = data.get('jtype', 'due')
        queryset = Judgement.objects.filter(wechatuser__openid=self.request.session['openid'])
        if jtype == 'due':
            queryset = queryset.filter(remind_date__lte=now.date(), judge__isnull=True).order_by('remind_date')
        elif jtype == 'no_due':
            queryset = queryset.filter(remind_date__gt=now.date(), judge__isnull=True).order_by('remind_date')
        else:
            queryset = queryset.filter(judge__isnull=False)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(MineJudgementListView, self).get_context_data()
        object_list = list(context.get('object_list').only('article_id'))
        object_ids = map(lambda x: x.article_id, object_list)
        object_list = ArticlePostedResults.active_objects.filter(id__in=object_ids).only('bigv_id', 'title', 'content', 'publish_date', 'article_source', 'score')
        v_ids = list(set(map(lambda x: x.bigv_id, object_list)))
        cache_bigv(v_ids)
        cache_options(object_ids, self.request.session['openid'])
        context.update({'object_list': object_list})
        context.update({'token': 'judge'})
        data = self.request.GET.copy()
        jtype = data.get('jtype', 'due')
        context.update({'jtype': jtype})
        return context 
