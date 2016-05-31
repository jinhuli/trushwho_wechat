# coding: utf-8

from django.views.generic import CreateView
from feedback.models import FeedBack
from feedback.forms import FeedBackForm


class FeedBackCreateView(CreateView):
    model = FeedBack
    form_class = FeedBackForm
    success_url = '/feedback/success/'

    def get_context_data(self, **kwargs):
        ftype = self.request.GET.copy().get('ftype', 0)
        context = super(FeedBackCreateView, self).get_context_data(**kwargs)
        context.update({'ftype': ftype})
        return context
