# coding: utf-8
'''
Created on 2016年4月28日

@author: likun
'''

from django.http import HttpResponse
from wxsdk.models import JSSdk

import json

def wx_config(request):
    data = request.GET.copy()
    url = data.get('url')
    openId = data.get('openId')
    callback = data.get('callback')
    jssdk = JSSdk(openId, url)
    return HttpResponse('%s(%s)' % (callback, json.dumps(jssdk.sign())), mimetype="application/json")

def escape(request):
    data = request.GET.copy()
    url = data.get('url')
    callback = data.get('callback')
    jssdk = JSSdk(url)
    return HttpResponse('%s(%s)' % (callback, json.dumps({'url':jssdk.url})), mimetype="application/json")
