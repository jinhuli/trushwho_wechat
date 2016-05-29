# coding: utf-8
'''
Created on 2016年5月24日

@author: likun
'''
from functools import wraps


def openid_exempt(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)
    wrapped_view.openid_exempt = True
    return wrapped_view