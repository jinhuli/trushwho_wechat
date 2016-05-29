# coding: utf-8
'''
Created on 2016年5月20日

@author: likun
'''
import markdown2
from django.template import Library
from django.core.cache import cache
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from common.constants import ARTICLE_JUDGEMENT_STATUS_KEY, ARTICLE_JUDGEMENT_DATE_KEY

register = Library()


@register.filter(is_safe=False)
def judge_status_css(value, openid):
    res = cache.get('{0}_{1}'.format(ARTICLE_JUDGEMENT_STATUS_KEY, openid))
    if res is None:
        return None
    t = ''
    status = res.get(value, 'normal')
    if status == 'wrong' or status == 'right':
        t = ' t2'
    if status is None:
        t = ' t1'
    return t


@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    return mark_safe(markdown2.markdown(force_text(value),
        extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))


@register.filter(is_safe=False)
def judge_date(value, openid):
    res = cache.get('{0}_{1}'.format(ARTICLE_JUDGEMENT_DATE_KEY, openid))
    if res is None:
        return None
    return res.get(value)
