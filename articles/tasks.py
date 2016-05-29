# coding: utf-8
'''
Created on 2016年5月16日

@author: likun
'''
from __future__ import division
from django.db import connection
from django.core.cache import cache
from django.db.models import Count
from multiprocessing.dummy import Pool
from celery import task
from articles.models import ArticlePostedResults, Judgement
from common.utils import debug
import time
from common.constants import ARTICLE_COMMENTS_KEY, JUDGE_RANK_KEY


@task
def build_score():
    st = time.time()
    queryset = ArticlePostedResults.active_objects.all()
    last = time.mktime(queryset.only('publish_date').latest('publish_date').publish_date.timetuple())
    cursor = connection.cursor()
    sql = "update {0} inner join \
    (select {0}.id, (((2000 - (({1} - UNIX_TIMESTAMP(`article_posted_results`.`publish_date`)) / 60.0)) * 0.05) + `big_vs`.`words_weight`) AS `level`\
    FROM {0} INNER JOIN `big_vs` ON ( {0}.`v_id` = `big_vs`.`v_id` ) WHERE {0}.`article_status` IN (2, 3)\
    ) as t1 on {0}.id = t1.id set score=t1.level".format('article_posted_results', last)
    cursor.execute(sql)
    cursor.fetchone()
    end = time.time()
    debug('task-score', end - st)
    
    
@task
def count_comments_():
    st = time.time()
    queryset = ArticlePostedResults.active_objects.all()
    print queryset.count()
    res = {}
    def _build(article):
        if article.comments.exists():
            count = article.comments.count()
            res.update({article.id: count})
    pool = Pool(8)
    pool.map(_build, queryset)
    pool.close()
    pool.join()
    cache.set(ARTICLE_COMMENTS_KEY, res)
    ed = time.time()
    debug('count_comments', ed - st)
    

@task
def build_rank():
    st = time.time()
    rank = Judgement.objects.values('wechatuser').annotate(count=Count('wechatuser')).order_by('wechatuser')
    rank = sorted(rank, cmp=cmp, key=lambda x: x['count'], reverse=True)
    num = len(rank)
    res = {}
    map(lambda x: res.update({rank[x - 1]['wechatuser']: '{0:.1%}'.format((num - x) / num)}), range(1, num + 1))
    cache.set(JUDGE_RANK_KEY, res)
    ed = time.time()
    debug('build_rank', ed - st)
    
    
if __name__ == '__main__':
    build_rank()
