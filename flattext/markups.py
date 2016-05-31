# coding: utf-8
'''
Created on 2016年5月30日

@author: likun
'''
try:
    from markdown2 import markdown
except:
    pass
from django.template import Template, Context
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _


class BaseMarkup(object):
    """An interface that flattext markup need support."""
    text_type = None  # string, for Flattext.text_type
    text_type_display = None  # string, for Flattext.get_text_type_display
    is_one_pass = True

    @classmethod
    def render(cls, text):
        raise NotImplementedError


class HTML(BaseMarkup):
    text_type = 'html'
    text_type_display = _(u'HTML')

    @classmethod
    def render(cls, text):
        return text


class PlainText(BaseMarkup):
    text_type = 'plain'
    text_type_display = _(u'Plain text')

    @classmethod
    def render(cls, text):
        return escape(text)


class MarkDown(BaseMarkup):
    text_type = 'markdown'
    text_type_display = _(u'Markdown')

    @classmethod
    def render(cls, text):
        return markdown(text)


class DjangoTemplate(BaseMarkup):
    text_type = 'django'
    text_type_display = _(u'Django template')
    is_one_pass = False

    @classmethod
    def render(cls, text, **kw):
        return Template(text).render(Context(kw))
