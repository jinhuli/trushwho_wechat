# coding: utf-8
'''
Created on 2016年5月20日

@author: likun
'''
from django.conf import settings
from django.http.response import HttpResponseRedirect
from accessrecord.models import AccessRecord
from wxsdk.models import WXSdk
from wechat.models import WechatUser



class RecordEventMiddleWare(object):
    def process_response(self, request, response):
        path = request.path
        if '/admin/' not in path and 'openid' in request.session:
            data = request.GET.copy()
            keyword = data.get('q', '')
            openid = request.session['openid']
            app = path.strip('/').split('/')[0]
            ip = request.META['REMOTE_ADDR']
            AccessRecord.objects.create(openid=openid, record=path, ip=ip, type=app, keyword=keyword)
        return response


class WechatUserMiddleWare(object):
    debug = settings.WECHATDEBUG
    def process_request(self, request):
        data = request.GET.copy()
        code = data.get('code', '')
        if code:
            sdk = WXSdk()
            result = sdk.oauth2_token(code)
            openid = result.get('openid')
            if openid:
                wechatuser, _ = WechatUser.objects.get_or_create(openid=openid)
                request.wechatuser = wechatuser
                request.session['openid'] = openid
        if self.debug:
            openid = 'o8Ak0wUaEsdqRw4RO3_qK8Np-SoI'
            wechatuser, _ = WechatUser.objects.get_or_create(openid=openid)
            request.wechatuser = wechatuser
            request.session['openid'] = openid
    
    def process_view(self, request, view_func, view_args, view_kwargs):
#         MicroMessenger
        if self.debug:
            return None
        if '/admin/' in request.path:
            return None
        if getattr(view_func, 'openid_exempt', False):
            return None
        if not hasattr(request, 'wechatuser'):
            url = '{0}://{1}{2}'.format(request.scheme, request.get_host(), request.get_full_path())
            sdk = WXSdk()
            redirect_url = sdk.oauth2_redirect_uri(url)
            return HttpResponseRedirect(redirect_url)
        