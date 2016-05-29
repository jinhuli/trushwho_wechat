# coding: utf-8

from django.views.generic import CreateView
from feedback.models import FeedBack


class FeedBackCreateView(CreateView):
    model = FeedBack
    fields = ['wechatuser', 'phone_number', 'email', 'content']
    success_url = '/feedback/success/'

