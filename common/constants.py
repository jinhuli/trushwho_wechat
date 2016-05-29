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
STATUS_CHOICES = (
    (0, _(u'无效')),
    (1, _(u'有效')),
)
MENU_TYPE_CHOICES = (
    ('click', _(u'点击推事件')),
    ('view', _(u'跳转URL')),
    ('scancode_push', _(u'扫码推事件')),
    ('scancode_waitmsg', _(u'扫码推事件且弹出“消息接收中”提示框')),
    ('pic_sysphoto', _(u'弹出系统拍照发图')),
    ('pic_photo_or_album', _(u'弹出拍照或者相册发图')),
    ('pic_weixin', _(u'弹出微信相册发图器')),
    ('location_select', _(u'弹出地理位置选择器')),
    ('media_id', _(u'下发消息（除文本消息）')),
    ('view_limited', _(u'跳转图文消息URL')),
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
ARTICLE_IS_JUDGEMENT_CHOICES = (
    (0, _(u'未判断')),
    (1, _(u'已判断')),
)
# 评论
ARTICLE_COMMENTS_KEY = 'wechat:article.comments.key'
# 正确判断
ARTICLE_JUDGEMENT_RIGHT_KEY = 'wechat:article.judgement.right.key'
# 错误判断
ARTICLE_JUDGEMENT_WRONG_KEY = 'wechat:article.judgement.wrong.key'
# 加入日历
ARTICLE_JUDGEMENT_CALENDAR_KEY = 'wechat:article.judgement.calendar.key'
# 判断状态
ARTICLE_JUDGEMENT_STATUS_KEY = 'wechat:article.judgement.status.key'

ARTICLE_JUDGEMENT_DATE_KEY = 'wechat:article.judgement.date.key'
# bigv
BIGVS_ALL_KEY = 'wechat:bigvs.all.key'

JUDGE_RANK_KEY = 'wechat:judge.rank.key'

PREDICTION_VIEWPOINT_CHOICES = (
    (u'rise', _(u'看多')),
    (u'drop', _(u'看空')),
    (u'bumpy', _(u'看平')),
)

# judge
JUDGEMENT_JUDGE_CHOICES = (
    ('wrong', _(u'错误')),
    ('right', _(u'正确')),
)

ACCESSRECORD_TYPE_CHOICES = (
    ('', _(u'首页')),
    ('articles', _(u'文章')),
    ('bigvs', _(u'大V')),
    ('feedback', _(u'反馈')),
    ('subscribe', _(u'订阅')),
    ('prediction', _(u'多空看板')),
    ('user', _(u'用户操作')),
)

