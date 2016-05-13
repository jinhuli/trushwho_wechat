# coding: utf-8
'''
Created on 2016年4月28日

@author: likun
'''

from django.utils.translation import gettext_lazy as _

# wechat
WECHAT_USER_SEX_CHOICES = (
    (0, _(U'未知')),
    (1, _(U'男')),
    (2, _(U'女')),
)

# bigv
BIGVS_DA_V_TYPE_CHOICES = (
    (1, _(u'个人')),
    (2, _(u'证券')),
    (3, _(u'NGO')),
)
BIGVS_IS_DEFAULT_CHOICES = (
    (0, _(u'默认名称')),
    (1, _(u'非默认名称')),
)

# article
ARTICLE_CATEGORY_CHOICES = (
    (1, _(u'新闻')),
    (2, _(u'博客')),
    (3, _(u'研报')),
)
ARTICLE_IS_CORRECT_CHOICES = (
    (-1, _(u'待处理')),
    (0, _(u'错误')),
    (1, _(u'正确')),
    (2, _(u'未到期')),
    (3, _(u'非预测')),
    (4, _(u'放弃判断')),
)
ARTICLE_EMOTION_LEVEL_CHOICES = (
    (1, _(u'非常乐观')),
    (2, _(u'乐观')),
    (3, _(u'中性')),
    (4, _(u'悲观')),
    (5, _(u'非常悲观')),
)
ARTICLE_PERIOD_CHOICES = (
    (1, _(u'天')),
    (2, _(u'周')),
    (3, _(u'月')),
    (4, _(u'季度')),
    (5, _(u'年')),
    (6, _(u'一年以上')),
)
ARTICLE_STATUS_CHOICES = (
    (-2, _(u'非抽样')),
    (1, _(u'初始（等待人工处理）')),
    (2, _(u'已人工处理')),
    (3, _(u'已发送')),
    (4, _(u'遗弃'))
)

PREDICTION_VIEWPOINT_CHOICES = (
    (u'rise', _(u'看多')),
    (u'drop', _(u'看空')),
    (u'bumpy', _(u'看平')),
)
