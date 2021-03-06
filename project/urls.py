# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
]

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('apps.blog.urls', namespace='news')),
    url(r'^services/', include('apps.services.urls', namespace='services')),
    url(r'^products/', include('apps.products.urls', namespace='products')),
    url(r'^clients/', include('apps.clients.urls', namespace='clients')),
    url(r'^company/', include('apps.company.urls', namespace='company')),

    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns
