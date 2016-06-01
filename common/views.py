# coding: utf-8
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.http import JsonResponse


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


class JSONView(JSONResponseMixin, View):
    pass


class WeChatView(TemplateView):
    def get_context_data(self, **kwargs):
        context_data = super(WeChatView, self).get_context_data(**kwargs)
        data = self.request.GET.copy()
        q = data.get('q', '')
        token = data.get('token', '')
        context_data.update({'q':q, 'token': token})
        return context_data
