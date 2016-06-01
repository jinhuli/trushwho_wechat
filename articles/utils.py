# coding: utf-8
'''
Created on 2016年5月23日

@author: likun
'''
from django.core.cache import cache
from django.db.models import Count
from django.core.paginator import Paginator
from django.conf import settings
from easy_thumbnails.files import get_thumbnailer
from wechat.models import Comment
from articles.models import Judgement
from bigvs.models import BigVs
from common.constants import ARTICLE_COMMENTS_KEY, ARTICLE_JUDGEMENT_RIGHT_KEY, ARTICLE_JUDGEMENT_WRONG_KEY\
, ARTICLE_JUDGEMENT_STATUS_KEY, ARTICLE_JUDGEMENT_CALENDAR_KEY, BIGVS_ALL_KEY, ARTICLE_JUDGEMENT_DATE_KEY


class CountPaginator(Paginator):
    def _get_count(self):
        return 100000;
    count = property(_get_count)
    

def cache_set(key, data):
    key_set = cache.get(key, {})
    key_set.update(data)
    cache.set(key, key_set, settings.NEVER_REDIS_TIMEOUT)
    

def cache_options(object_ids, openid):

    comments = Comment.objects.filter(object_id__in=object_ids, content_type__model='articlepostedresults')\
                                .values('object_id').annotate(count=Count('object_id')).order_by('object_id')
    comment_set = {}
    map(lambda x: comment_set.update({x['object_id']: x['count']}), comments)
    cache_set(ARTICLE_COMMENTS_KEY, comment_set)

    right, wrong, calendar = {}, {}, {}
    def build(x):
        judge = x['judge']
        if judge == 'right':
            right.update({x['article_id']: x['count']})
        elif judge == 'wrong':
            wrong.update({x['article_id']: x['count']})
        else:
            calendar.update({x['article_id']: x['count']})

    judgements = Judgement.objects.filter(article__id__in=object_ids).values('article_id', 'judge').annotate(count=Count('article_id')).order_by('article_id', 'judge')
    map(lambda x: build(x), judgements)
    cache_set(ARTICLE_JUDGEMENT_RIGHT_KEY, right)
    cache_set(ARTICLE_JUDGEMENT_WRONG_KEY, wrong)
    cache_set(ARTICLE_JUDGEMENT_CALENDAR_KEY, calendar)

    judgements_status = Judgement.objects.filter(article__id__in=object_ids, wechatuser__openid=openid).values('id', 'article_id', 'judge', 'remind_date', 'hint_text')
    status_set = {}
    map(lambda x: status_set.update({x['article_id']: x['judge']}), judgements_status)
    cache_set('{0}_{1}'.format(ARTICLE_JUDGEMENT_STATUS_KEY, openid), status_set)
    
    judge_set = {}
    map(lambda x: judge_set.update({x['article_id']: {'remind_date': x['remind_date'], 'hint_text': x['hint_text'], 'id': x['id']}}), judgements_status)
    cache_set('{0}_{1}'.format(ARTICLE_JUDGEMENT_DATE_KEY, openid), judge_set)


def cache_bigv(v_ids):
    bigvs = BigVs.objects.filter(v_id__in=v_ids).only('v_id', 'name', 'words_weight', 'headimg', 'initials')
    res = {}
    for b in bigvs:
        bd = {}
        bd.update({'name': b.name})
        bd.update({'words_weight': b.words_weight})
        bd.update({'initials': b.initials})
        if b.headimg:
            bd.update({'headimg': get_thumbnailer(b.headimg)['avatar'].url})
        res.update({b.v_id: bd})
        
    cache_set(BIGVS_ALL_KEY, res)

