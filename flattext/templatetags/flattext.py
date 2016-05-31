# coding: utf-8
'''
Created on 2016年5月30日

@author: likun
'''
# -*- coding: utf-8 -*-

from django.template import Library
from flattext.models import FlatText
from common.utils import debug

register = Library()

@register.simple_tag
def flattext(slug, modes=''):
    """Render a flattext by slug."""
    # modes = modes.split()
    # silence = 'silence' in modes
    try:
        # where the db hit actually occurs
        text = FlatText.objects.get(slug=slug).render()
    except Exception, e:
        debug('flattext', u'failed to render flattext "%s": %s' % (slug, e))
        text = ''
    return text
