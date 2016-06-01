from django.conf import settings
from django.conf.urls import include, url, patterns
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
    url(r'^subscribe/', include('subscribe.urls')),
    url(r'^prediction/', include('prediction.urls')),
    url(r'^user/', include('wechat.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

    urlpatterns += patterns(
        '',
        url(r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    )