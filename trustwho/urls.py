from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'trustwho.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bigvs/', include('bigvs.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
