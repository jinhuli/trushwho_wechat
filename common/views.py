# coding: utf-8
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect

from wxsdk.models import WXSdk
from wechat.models import WechatUser
from common.utils import debug


class WeChatMixin(object):
    
    def validate_code(self, request):
        data = request.GET.copy()
        code = data.get('code', '')
        sdk = WXSdk()
        if code:
            result = sdk.oauth2_token(code)
            self.openid = result.get('openid')
            debug('validate', self.openid)
            if not WechatUser.objects.filter(openid=self.openid).exists():
                WechatUser.objects.create(openid=self.openid)
        else:
            url = 'http://{0}{1}'.format(request.get_host(), request.path)
            return sdk.oauth2_redirect_uri(url)

class WeChatView(WeChatMixin, TemplateView):
    
    def get(self, request, *args, **kwargs):
        redirect_url = self.validate_code(request)
        if redirect_url: return HttpResponseRedirect(redirect_url)
        return super(WeChatView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context_data = super(WeChatView, self).get_context_data(**kwargs)
        context_data.update({'openid': self.openid})
#         context_data.update({'openid': 'ojhvmt8R8uQwkvR-tHzzy-M_rcvI'})
        q = self.request.GET.copy().get('q', '')
        context_data.update({'q':q})
        return context_data


class WeChatDetailView(WeChatMixin, DetailView):
    
    def get(self, request, *args, **kwargs):
        redirect_url = self.validate_code(request)
        if redirect_url: return HttpResponseRedirect(redirect_url)
        return super(WeChatDetailView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context_data = super(WeChatDetailView, self).get_context_data(**kwargs)
        context_data.update({'openid': self.openid})
        return context_data
