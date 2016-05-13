# coding: utf-8
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.http import JsonResponse

from wxsdk.models import WXSdk
from wechat.models import WechatUser
from common.utils import debug
from accessrecord.models import AccessRecord
from django.views.generic.list import ListView


class WeChatMixin(object):
    openid = None
    debug = False
    def validate_code(self, request):
        data = request.GET.copy()
        code = data.get('code', '')
        sdk = WXSdk()
        if code:
            result = sdk.oauth2_token(code)
            self.openid = result.get('openid')
            debug('WeChatMixin', self.openid)
            if self.openid and (not WechatUser.objects.filter(openid=self.openid).exists()):
                WechatUser.objects.create(openid=self.openid)
        else:
            url = 'http://{0}{1}'.format(request.get_host(), request.get_full_path())
            if self.debug:
                self.openid = 'ojhvmt8R8uQwkvR-tHzzy-M_rcvI'
            else:
                return sdk.oauth2_redirect_uri(url)
            

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            safe=False,
            ** response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context
    
class JSONListView(JSONResponseMixin, ListView):
    
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
    
    
class WeChatView(WeChatMixin, TemplateView):
    
    def get(self, request, *args, **kwargs):
        redirect_url = self.validate_code(request)
        if redirect_url: return HttpResponseRedirect(redirect_url)
        return super(WeChatView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context_data = super(WeChatView, self).get_context_data(**kwargs)
        context_data.update({'openid': self.openid})
        data = self.request.GET.copy()
        q = data.get('q', '')
        token = data.get('token', '')
        context_data.update({'q':q, 'token': token})
        return context_data


class WeChatListView(WeChatMixin, ListView):
    
    def get(self, request, *args, **kwargs):
        redirect_url = self.validate_code(request)
        if redirect_url: return HttpResponseRedirect(redirect_url)
        AccessRecord.objects.create(openid=self.openid, record=request.path)
        return super(WeChatListView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context_data = super(WeChatListView, self).get_context_data(**kwargs)
        context_data.update({'openid': self.openid})
        return context_data


class WeChatDetailView(WeChatMixin, DetailView):
    
    def get(self, request, *args, **kwargs):
        redirect_url = self.validate_code(request)
        if redirect_url: return HttpResponseRedirect(redirect_url)
        AccessRecord.objects.create(openid=self.openid, record=request.path)
        return super(WeChatDetailView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context_data = super(WeChatDetailView, self).get_context_data(**kwargs)
        context_data.update({'openid': self.openid})
        return context_data
    
    
class WechatCreateView(WeChatMixin, CreateView):
    
    def get(self, request, *args, **kwargs):
        redirect_url = self.validate_code(request)
        if redirect_url: return HttpResponseRedirect(redirect_url)
        return super(WechatCreateView, self).get(request, *args, **kwargs)

