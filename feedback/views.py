# coding: utf-8

from common.views import WechatCreateView
from feedback.models import FeedBack
from wechat.models import WechatUser


class FeedBackCreateView(WechatCreateView):
    model = FeedBack
    fields = ['wechatuser', 'phone_number', 'email', 'content']
    success_url = '/feedback/success/'
    
    def get_context_data(self, **kwargs):
        context_data = super(FeedBackCreateView, self).get_context_data(**kwargs)
        if self.openid:
            wechatuser = WechatUser.objects.get(openid=self.openid)
            context_data['wechatuser_id'] = wechatuser.id
        return context_data
